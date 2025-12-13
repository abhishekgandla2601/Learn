# class variables = Shared among all instances of a class
#                   Defined outside the constructor

#                   instance variables are defined inside the constructor
#                   class variables are defined outside the constructor
#                   Allow you to share data among all objects created from that class

class student:

    # class variables are defined outside a constructor
    class_year = 2024
    num_students = 0
    def __init__(self, name, age): # self  - object we are currently working with
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Spongebob", 30)
student2 = student("Patrick", 35)
student3 = student("Squidward", 55)
student4 = student("Sandy", 27)

print(student1.name)
print(student1.age)
print(student.class_year)
print()
print(student2.name)
print(student2.age)
print(student.class_year)

print(student.num_students)

print(f"My graduating class of {student.class_year} has {student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
