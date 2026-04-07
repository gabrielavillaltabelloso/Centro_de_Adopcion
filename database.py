import config

def get_available_dogs():
    conn = config.get_db_connection()
    cur = conn.cursor()
    # 5 columnas: id(0), name(1), age(2), breed(3), image_url(4)
    cur.execute("SELECT id, name, age, breed, image_url FROM Dog WHERE adopted = 0")
    dogs_data = cur.fetchall()
    cur.close()
    conn.close()
    return dogs_data

def get_dog_by_id(dog_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, breed, image_url FROM Dog WHERE id = %s", (dog_id,))
    dog_data = cur.fetchone()
    cur.close()
    conn.close()
    return dog_data

def register_adoption_transactional(dog_id, adopter_name, adopter_lastname, address, id_card):
    conn = config.get_db_connection()
    if not conn: return False
    
    cur = conn.cursor()
    try:
        conn.autocommit = False 
        
        # 1. Registrar o actualizar a la Persona (Evita error de DUI duplicado)
        # Si el id_card ya existe, simplemente actualiza el nombre
        cur.execute("""
            INSERT INTO Person (name, lastName, id_card) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE name = VALUES(name), lastName = VALUES(lastName)
        """, (adopter_name, adopter_lastname, id_card))
        
        # Obtenemos el ID de la persona (sea nueva o ya existente)
        cur.execute("SELECT id FROM Person WHERE id_card = %s", (id_card,))
        person_id = cur.fetchone()[0]
        
        # 2. Registrar al Adoptante (INSERT IGNORE por si ya estaba en esta tabla)
        cur.execute("INSERT IGNORE INTO Adopter (person_id, address) VALUES (%s, %s)", 
                   (person_id, address))
        
        # 3. Registrar la relación en la tabla Adoption
        cur.execute("INSERT INTO Adoption (adopter_id, dog_id, adoption_date) VALUES (%s, %s, NOW())", 
                   (person_id, dog_id))
        
        # 4. Marcar al perro como adoptado
        cur.execute("UPDATE Dog SET adopted = 1 WHERE id = %s", (dog_id,))
        
        conn.commit() 
        return True
        
    except Exception as e:
        if conn: conn.rollback() 
        print(f"Error específico en la transacción: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def get_adoption_history():
    conn = config.get_db_connection()
    cur = conn.cursor()
    # Traemos P.id como primer elemento para que el botón de eliminar tenga el ID correcto
    query = """
        SELECT 
            P.id,
            P.name, 
            P.lastName, 
            D.name, 
            D.breed, 
            A.adoption_date
        FROM Adoption A
        INNER JOIN Person P ON A.adopter_id = P.id
        INNER JOIN Dog D ON A.dog_id = D.id
        ORDER BY A.adoption_date DESC
    """
    try:
        cur.execute(query)
        history = cur.fetchall()
        return history
    except Exception as e:
        print(f"Error en la consulta de historial: {e}")
        return []
    finally:
        cur.close()
        conn.close()

def delete_person_by_id(person_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    try:
        conn.autocommit = False
        
        # A. Buscamos los perros que esta persona tenía para volver a ponerlos como NO adoptados
        cur.execute("SELECT dog_id FROM Adoption WHERE adopter_id = %s", (person_id,))
        dogs = cur.fetchall()
        for dog in dogs:
            cur.execute("UPDATE Dog SET adopted = 0 WHERE id = %s", (dog[0],))

        # B. Borrar de la tabla Adoption primero (evita error de llave foránea)
        cur.execute("DELETE FROM Adoption WHERE adopter_id = %s", (person_id,))
        
        # C. Borrar de la tabla Adopter
        cur.execute("DELETE FROM Adopter WHERE person_id = %s", (person_id,))
        
        # D. Finalmente borrar de la tabla Person
        cur.execute("DELETE FROM Person WHERE id = %s", (person_id,))
        
        conn.commit()
        return True
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error al eliminar: {e}")
        return False
    finally:
        cur.close()
        conn.close()