# List

'''
Lists are used to store multiple items in a single variable.
Lists are mutable, meaning they can be changed after their creation.
Lists are defined by having values between square brackets [].
Lists can contain items of different data types.
Lists can be nested, meaning a list can contain other lists as its elements.
Lists are ordered, meaning the items have a defined order, and that order will not change.
Lists allow duplicate values.
Lists are indexed, meaning each item in a list has a defined index that can be used to access it.
Lists can be sliced, meaning you can access a range of items in a list.
Lists have many built-in methods that can be used to manipulate them.
'''

marks = [3, 5,6, "Harry", True]#order is maintained, indexed, mutable, allows duplicate values
print(marks)
print(type(marks))

print(marks[0])# accessing list elements
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Negative Indexing
print(marks[-1])# accessing list elements from the end
print(marks[-2])

print(marks[-3])# negative indexing starts from -1
print(marks[len(marks)-3])#positive indexing


if 7 in marks:
    print("Yes")
else:
    print("No")
    
    
if "6" in marks:
    print("Yes")
else:
    print("No")
    
# print(marks[1:len(marks)])    
print(marks[1: ])# slicing
print(marks[1:4])
print(marks[1:4:2])






# List comprehension

'''
List comprehensions are used for creating new lists from iterables like lists,
tuples, dictionaries, sets, and even in arrays and strings.
'''
lst = [i*i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)

# what is list comprehension?
# List comprehension is a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The expressions can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for
# and if clauses which follow it.
# List comprehension is generally more compact and faster than normal functions and loops for creating lists.
# List comprehension is a powerful tool for creating lists in a single line of code.
# List comprehension can also be used to create lists from other iterables like strings, tuples, and dictionaries.
# Example:
lst = [i for i in 'abhishek']
print(lst)
# Output: ['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']
# Example:
d = {'a':1, 'b':2, 'c':3}
lst = [k for k,v in d.items()]
print(lst)
# Output: ['a', 'b', 'c']
# Example:
t = (1,2,3,4)
lst = [i*i for i in t]
print(lst)
# Output: [1, 4, 9, 16]

'''
The simple way to understand list comprehension is:
newlist = []
for item in iterable:
    if condition:
        newlist.append(expression)
        
'''

'''
simple definition of list comprehension is:
newlist = [expression for item in iterable if condition]
'''