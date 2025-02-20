class Person:
    def __init__(self, name, age, size, kg = 0 ):
        self.name = name
        self.age = age
        self.size = size
        self. kg = kg

    def evlilik(self, age):
        if age < 18:
            print("Evlilik icin uygun degil")
        else:
            print("Evlilik icin uygun yas!")

person1 = Person("Ferdi", 28 ,32)
print(person1.name ,person1.age, person1.size, person1.kg)
person1.evlilik(28)

person2 = Person("Bahar", 29, 18)
person2.evlilik(11)