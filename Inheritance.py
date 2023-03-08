# INHERITANCE IN PYTHON. Types; single inheritance, multilevel, multipe inheritance.
   # 1 SINGLE INHERITANCE.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"

dog = Dog("Buddy", "Labrador")
print(dog)
 #MULTI LEVEL INHERITANCE. /Here class B inherits A, C inherits B, D inherit C and so forth.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"

class DomesticAnimal(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Domestic Animal")
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"

class Dog(DomesticAnimal):
    def __init__(self, name, breed, toy):
        DomesticAnimal.__init__(self, name, breed)
        self.toy = toy

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species} who loves to play with a {self.toy}"

dog = Dog("Buddy", "Labrador", "bone")
print(dog)
# 3 MULTIPLE INHERITANCE.
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
        
    def mother_info(self):
        return f"Mother's name is {self.mother_name}"

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def father_info(self):
        return f"Father's name is {self.father_name}"

class Child(Mother, Father):
    def __init__(self, child_name, mother_name, father_name):
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name = child_name

    def child_info(self):
        return f"Child's name is {self.child_name}"

child = Child("Tommy", "Jane", "John")
print(child.child_info())
print(child.mother_info())
print(child.father_info())
