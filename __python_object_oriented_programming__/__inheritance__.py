# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(parent)
from Learn.python.mark33 import name1


class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(animal):
    def speak(self):
        print("WOOF!")
class cat(animal):
    def speak(self):
        print("MEOW!")
class mouse(animal):
    def speak(self):
        print("SQUEEK!")
dog = Dog("Scooby")
cat= cat("Tom")
mouse = mouse("Jerry")

print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()


print(cat.name)
print(cat.is_alive)

cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)

mouse.eat()
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()
