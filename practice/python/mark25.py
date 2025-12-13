#variable length argument

'''
Sometime we may need to pass more arguments than
those defined in the actual function.
This can be done using variable length arguments.
'''

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("The average is", sum/len(numbers))
    
# average(5,6, 7)


# def name(**name):
#     print(type(name))
#     print("Hello", name["fname"], name["mname"], name["lname"])

# name(mname = "Barry", lname = "Allen", fname = "Eobard")



def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        
    # print("The average is", sum/len(numbers))
    return sum/len(numbers)
    
c = average(5,6, 7,1)
print(c)

# return statement in python
'''
The return statement is used to exit a function and return a value.
When a return statement is executed, the function terminates
and the value is returned to the caller.
If there is no return statement, the function will return None.
A function can have multiple return statements.
A function can return multiple values.
'''

