# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
#
# def func1():
#     a  = 1 # local declaration
#     print(a)
#
# def func2():
#     b = 2# local declaration
#     print(b)
#
# func1()
# func2()
#
# def fun1():
#     x = 1
#
#     def fun2():
#         print(x)
#     fun2()
# fun1()


# global scope

def fun1():
    print(x)

def fun2():
    print(x)
x = 3# global decalration
fun1()
fun2()


from math import e
print(e)

# if there is a variable of local version and global version, it will accept the global version only