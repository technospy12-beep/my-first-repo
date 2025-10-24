from abc import ABC, abstractmethod




class shape(ABC):
    

    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self,radius):
        self.radius=radius


    def area(self):
            return self.radius **2 *3.14


class square(shape):
    def __init__(self,side):
        self.side=side



    def area(self):
        return self.side * self.side


class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height


    def area(self):
            return  self.base * self.height * 0.5
    


class Pizza(circle,shape):
     def __init__(self,radius,toppings):
         super().__init__(radius)
         self.toppings=toppings




shapes = [circle(4), square(5), triangle(6,7),Pizza("pepperoni",8)]


for shape in shapes:
    print(f"{shape.area()} cm")



