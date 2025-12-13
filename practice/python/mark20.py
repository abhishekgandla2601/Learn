# while loop in python

'''
While loops execute statements while the codition is True.
As soon as the condition becomes False, 
the interpreter comes out of the while loop. 
'''

# i = 0

# while(i <= 3):
    
#     print(i)
#     i = i + 1

# print('Done with the loop')


# i = int(input("Enter a number:"))

# while (i <= 38):
#     i = int(input("Enter a number:"))

#     print(i)
    
# print('Done with the loop')

'''
The difference between for loop and while loop is:
for loop is used when the number of iterations is known.
while loop is used when the number of iterations is not known.
for example:
for i in range(10): # number of iterations is known
    print(i)
while (i < 10): # number of iterations is not known
    print(i)
    i = i + 1
'''
# decrementing using while loop
# count = 5

# while(count > 0):
#     print(count)
#     count = count - 1
    
'''
Depending upon the while loop condition, we need to either incement 
or decrement the counter vairable or the loop will continue forever.
'''



#else with while loop
'''
We can even use the else statement with the while loop.
Essential what the else statement does is that as soon as the while loop
conditon becomes False, the interpreter comes out of the while loop and
the else statement is executed.
'''
count = 5
while(count > 0):
    print(count)
    count = count -1 
else:
    print("I am inside else")

'''
do-while loop is not present in python.
do-while loop is present in other programming languages like C, C++, Java etc.
what do-while loop does is that it executes the statements at least once
and then checks the condition.

do{
    #loop body
}while(condition);
'''

#how to emulate do-while loop in python
'''
we can emulate do-while loop in python using while loop.
we can use while(True) and then
use break statement to come out of the loop.
'''
while(True):
    print("I am inside do-while loop")
    num = int(input("Enter a number:"))
    if(num > 100):
        break
print("I am outside do-while loop")
