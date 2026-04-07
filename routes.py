from flask import Flask, render_template, request, redirect, url_for
import database
import models

app = Flask(__name__)

@app.route('/')
def index():
    # Recuperamos los perros del catálogo real (que no han sido adoptados)
    dogs_data = database.get_available_dogs()
    
    # Creamos la lista pasando los parámetros necesarios para el objeto Dog
    available_dogs = [models.Dog(row[0], row[1], row[2], row[3], row[4]) for row in dogs_data]
    
    return render_template('catalogo.html', dogs=available_dogs)

@app.route('/adoptar/<int:dog_id>')
def form_adopcion(dog_id):
    dog = database.get_dog_by_id(dog_id)
    if not dog:
        return "Perrito no encontrado", 404
    
    # Creamos el objeto para mostrarlo en el formulario de confirmación
    dog_obj = models.Dog(dog[0], dog[1], dog[2], dog[3], dog[4])
    return render_template('confirmacion.html', dog=dog_obj)

@app.route('/historial')
def historial():
    # Ahora la función devuelve el ID de la persona para poder eliminarla
    adopciones = database.get_adoption_history()
    return render_template('historial.html', adopciones=adopciones)

@app.route('/confirmar_adopcion', methods=['POST'])
def procesar_adopcion():
    # Recibimos datos del formulario de la web
    dog_id = request.form['dog_id']
    name = request.form['name']
    lastname = request.form['lastname']
    address = request.form['address']
    id_card = request.form['id_card']
    
    # Ejecutamos la lógica de negocio modular (incluye validación de persona existente)
    success = database.register_adoption_transactional(dog_id, name, lastname, address, id_card)
    
    if success:
        dog = database.get_dog_by_id(dog_id)
        # Respuesta simple de éxito con enlace para volver
        return f"<h1>¡Felicidades! Has adoptado a {dog[1]} exitosamente.</h1><a href='/'>Volver al catálogo</a>"
    else:
        return "Error al procesar la adopción. Es posible que el perro ya no esté disponible o haya un error en los datos.", 400

# --- NUEVA RUTA PARA ELIMINAR ADOPTANTE ---
@app.route('/eliminar_persona/<int:person_id>', methods=['POST'])
def eliminar_persona(person_id):
    # Llama a la función que borra en cascada (Adoption -> Adopter -> Person)
    # y libera al perro (adopted = 0)
    success = database.delete_person_by_id(person_id)
    
    if success:
        # Si todo sale bien, refrescamos el historial
        return redirect(url_for('historial'))
    else:
        # Error en caso de que la transacción falle
        return "No se pudo eliminar al adoptante", 400

if __name__ == '__main__':
    # Ejecución del servidor en modo debug
    app.run(debug=True, host='0.0.0.0', port=5000)