# function = a block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):# parameter, position of the parameter is matter
    print(f"Happy Birthday to {name}!")
    print("Welcome to Happy Birthday!")
    print(f"You are {age} years old!")
happy_birthday("Bro", 23)# argument


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")
display_invoice("Abhishek", 50.52, "01/05/2026")

# return = statement used to end a function
#           and send a result back to the caller
def add(x,y):
    z=x+y
    return z
def subtract(x,y):
    z=x-y
    return z
def multiply(x,y):
    z=x*y
    return z
def divide(x,y):
    z=x/y
    return z
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
