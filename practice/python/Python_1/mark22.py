#Functions
'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

#types of functions in python
'''
Built-in functions
User-defined functions
Anonymous functions
'''
# Built-in functions
'''
Python has many built-in functions like:
print()
input()
type()
int()
str()
float()
len()
list()
dict()
set()
tuple()
range()
'''
# User-defined functions
'''
A user-defined function is a function that is defined by the user.
It is defined using the def keyword.
It can take parameters and return values.
'''

a = 9 
b= 8

gmean = (a*b)/(a+b)
print(gmean)
c = 8

d = 7
gmean2 = (c*d)/(c+d)
print(gmean)


def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
a= 9
b= 8 
if a>b:
    print("1st number is greater")
else:
    print("2nd number is greater or equal")
calculategmean(a,b)
c=8
d=7

if c>d:
    print("1st number is greater")
else:
    print("2nd number is greater or equal")
calculategmean(c,d)