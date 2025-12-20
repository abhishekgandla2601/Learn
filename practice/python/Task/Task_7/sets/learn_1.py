# creating a set
# creating an empty set
st = set()

#creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

# getting sets lengths

print(len(st))

# checking an item 
print("Does set st contain item3? ", "item3" in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# adding items to a set
st.add('item5')
print(st)

fruits.add('lime')
print(fruits)

# add multiple items using update()
st.update(['item5', 'item6', 'item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)
print(vegetables)

# removing items from a set
st.remove('item2')

# The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

print(removed_item)


# clearing items in a set
st.clear()

print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st

del fruits

# converting list to set
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# joining sets
# union or update

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

print(st3)

# finding intersection items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'}

# checking subset superset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True

# checking the difference between two sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set()
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2

# symmetric differencebetween two sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

# joining sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1)) # False