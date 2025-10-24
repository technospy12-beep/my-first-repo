class Animal:
    alive=True


class Dog(Animal):
    def speak(self):
        print("Woof!")
      

class cat(Animal):
    def speak(self):
        print("Meaow!")



class Car:
    def speak(self):
        print("Honk!")




animals=[Dog(),cat(),Car()]
for animal in animals:
    animal.speak()

print(Animal.alive)

