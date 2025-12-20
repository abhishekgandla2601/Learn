# Create an empty tuple
empty_tuple = ()
print(empty_tuple)

names = ("me", "Abhishek")

print(names)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('sister1', 'sister2', 'sister3', 'sister4')
brothers = ('brother1', 'brother2', 'brother3', 'brother4')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters 
print(siblings)

# How many siblings do you have?
print('number of siblings: ',len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = ('brother1', 'brother2', 'brother3', 'brother4', 'sister1', 'sister2', 'sister3', 'sister4', 'father', 'mother')
print(siblings)
print(family_members)

# Unpack siblings and parents from family_members
print("Siblings: ",family_members[0:-2])
print("Parents: ",family_members[-2:])

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "cherry")
vegetables = ("tomato", "potato", "green chilli")
animal = ("meat", "chicken", "fish")

food_stuff_tp = fruits + vegetables + animal

print("Food stuff: ",food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_tp))
print("Middle item: ", len(food_stuff_tp) // 2, "=", food_stuff_tp[4])

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[0:3]
print("First three items = ", first_three )
last_three = food_stuff_tp[-3:]
print("Last_three items = ", last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp