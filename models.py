class Dog:
    def __init__(self, id, name, age, breed, image_url='perrito.jpg'):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed
        self.image_url = image_url

class Adopter:
    def __init__(self, adopter_id, name, lastName, address, id_card=None):
        self.adopter_id = adopter_id # Referecia a Person.id
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id_card = id_card