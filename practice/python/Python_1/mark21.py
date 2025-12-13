#break and continue statements in python

'''
The break statement is used to terminate the loop
when some condition is met.
The continue statement is used to skip the current iteration
and continue with the next iteration of the loop.
'''

# for i in range(12):
#     print("5 x", i, "=", 5* (i+1))
#     if i == 10:
#         break
# print('leave the loop and come out of it')

# continue statement


# for i in range(12):
#     if i == 10:
#         print('Skip the itration')
#         continue# skip the current iteration and continue with the next iteration
#     print("5 x", i, "=", 5* i)

# emulating do-while loop in python

i = 0
while True:# infinite loop
    print(i)
    i = i + 1
    if(i % 100 ==0):
        break


'''
do while is a loop in which a set of instructions 
will execute at least once and then
repetition of loop's body will depend on the while loop.
It is also known as exit-controlled loop.
'''