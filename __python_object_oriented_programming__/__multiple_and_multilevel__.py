# multiple inheritance = inherit from more than one parent class
#                           C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class prey:
    def flee(self):
        print("This animal is fleeing")

class predator:
    def hunt(self):
        print("This animal is hunting")

class rabbit:
    pass

class hawk:
    pass

class fish(prey, predator):
    pass

rabbit_ = rabbit()

hawk_ = hawk()

fish_ = fish()

rabbit_ = rabbit("Bugs")
hawk_ = hawk("Tony")

fish_ = fish("Nemo")

hawk.hunt()