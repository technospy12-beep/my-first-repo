class Student:
    class_year = 2025




    def __init__(self, name, age):
       self.name = name
       self.age = age


student1 = Student("Evan", 13)
student2 = Student("James", 22)
print(student1.name)
print(student1.age)
print(student1.class_year)