class Animal:
    def __init__(self):
        print("fucking dog")

    def speak(self):
        print("fucking sound")

 
class Dog(Animal):
    def __init__(self, name):
       self.name = name
    def speak(self):
        print(f"{self.name}: Aw Aw")
class Askal(Dog):
    def __init__(self, name):
        super().__init__(name)

class Shitzu(Dog):
    def __init__(self, name):
        super().__init__(name)

class Fox (Dog):
    def __init__(self, name):
        super().__init__(name)
zoo = []
for i in range(5):
    animal = Animal()
    zoo.append(Fox("fox you"))
    zoo.append(Animal())
    zoo.append(Dog("aik"))
    zoo.append(Dog("kia"))
    zoo.append(Dog("Krys"))

for animal in zoo:
    animal.speak()