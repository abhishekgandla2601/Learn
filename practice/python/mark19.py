#loops
'''
Sometimes a programmer wants to execute a group of statements
a certain number of times.
This can be done using loops.
'''
'''
for loop 
while loop 
nested loop
'''

# For loop in python
'''
For loops can iterate over a sequence of iterable objects in python.
Iterating over a sequence is nothing but iterating over 
strings,
lists,
tuples,
sets and dictionaries.
'''
# print 1 to 20 numbers

# print(1)
# print(2)
# print(3)
# print(4)

# # for loop, looping through a string:
# name = 'Abhishek'
# for i in name:
# # for every character in name print that character
# # if list, for every element in list print that element
#     print(i)
#     if(i == 'b'):
#         print("This is something special!")
        
#for loop, looping through a list:

# colors = ['Red', 'Green', 'Blue', 'Yellow']

# for x in colors:
#     print(x)
#     for i in x:
#         print(i)
        
# range():

# for k in range(5):# 0-5(only one parameter)
#     print(k+1)
# print()
# for m in range(1,9):
#     print(m)

for k in range(1,12,3):# what is the use of 3rd parameter?
    #the 3rd parameter is called step parameter
    #it defines the increment value
    #by default it is 1
    #if we want to increment by 3 then we can use 3rd parameter
    print(k)