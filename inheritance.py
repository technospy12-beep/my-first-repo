class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True


    def eat(self):
        print(f"{self.name} is eating"
              f"")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("Meow!!")

class Mouse(Animal):
    def speak(self):
        print("sch..sch!!")


dog = Dog("chilly")
cat = Cat("pookie")
mouse = Mouse("mickey")


mouse.speak()