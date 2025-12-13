# function arguments

def average(a,b):# parameters
    print("The average is", (a+b)/2)

average(4,6)# arguments

# default arguments
def average(a=9, b=1):
    print("The average is", (a+b)/2)

average(1,5)
average(b=9)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello", fname, mname, lname)

name("Amy", "Agarwal", "Jain")


'''
# Keyword Arguments
We can provide arguments with key = value, this way the interpreter recognizes the
arguments by the parameter name.
Hence, the order in which the arguments are passed does not matter.
'''

'''
Required Arguments
In case we don't pass the arguments with a key = value syntax,
then ir is necessary to pass the arguments in the correct 
positional order and the number of arguments passed sould match with actual function definition
'''

# Examples:
#When number of arguments passes does not match to the actual function
# definiton

def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name("peter", "Quill")
