import random

# print(help(random))
low = 1
high = 100
options = ("rock", "paper", "scissors")
cards =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.randint(1,6)# (1,6) is the range
# number = random.randint(low, high)
# print(number)

# number = random.random()# gives the float values
# print(number)

# option = random.choice(options)
#
# print(option)

random.shuffle(cards)
print(cards)