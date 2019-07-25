class Animal:
    def __init__(self,name,species,age, alive, nai): #constructor method
        self.name = name
        self.species = species
        self.age = age
        self.alive = alive
        self.number_animal_eaten = nai

    #class methods
    def sleep(self):
        return 'zzz'

    def eat(self,food):
        return 'nom NOM nom NOM this was some good ' + food

    def potty(self):
        return "lmao"

    def get_name(self):
        return self.name

    def change_name(self, name):
        self.name = name