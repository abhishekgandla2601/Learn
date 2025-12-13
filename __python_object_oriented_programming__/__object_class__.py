# object = A "bundle" of related attributes (variables) and methods(functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects
# A method is a function which is belongs to an object
# class = (blueprint) used to design the structure and layout of an object

from car import car
from __methods__ import car
# car object

car1 = car("Mustang", 2024, "red", False)
car2 = car("Corvette", 2025, "blue", True)
car3 = car("Charger", 2026, "yellow", True)

print(car1.model)# . attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)# . attribute access operator
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)



car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()