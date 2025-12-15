# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
fd = 7//3
print(fd)
print(type(fd))
c_fd = float(fd)
print(type(c_fd))
print(c_fd)

if fd == c_fd:
    print(True)
else:
    print(False)
    
    
print(fd is c_fd)# int and float are different types

# Check if type of '10' is equal to type of 10
num = 10
str_num = '10'
print(type(num) == type(str_num))# False

#Check if int('9.8') is equal to 10
nine_point_eight = '9.8'
ten = 10
# converting string to float first then to int
c_nine_point_eight = int(float(nine_point_eight)) 

print(c_nine_point_eight == ten) # False