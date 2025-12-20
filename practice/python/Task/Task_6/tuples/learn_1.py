# creating an empty tuple
empty_tuple = ()

# tuple constructor
empty_tuple = tuple()

# tuple with initial values
tp1 = ('item1', 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
len(tp1)

# accessing tuple items
first_item = tp1[0]
second_item = tp1[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(len(tp1))
print(last_index)

# negative indexing
first_item = tp1[-3]
first_item = tp1[-2]

first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# changing tuples into list
fruits = list(fruits)
print(type(fruits))
print(fruits[0])

# checking an item in tuple 

tpl = ('item1', 'item2', 'item3', 'item4')
print('item1' in tpl)

# joining tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ( 'item4', 'item5', 'item6')
# joining the tuples
print(tpl1 + tpl2)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'potato', 'cabbage', 'onion', 'carrot')

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


# deleting tuples

tpl1 = ('item1', 'item2', 'item3')

del tpl1
# print(tpl1) -- gives you an error

fruits = ('banana', 'orange', 'manago', 'lemon')
del fruits
# print(fruits) -- gives you an error