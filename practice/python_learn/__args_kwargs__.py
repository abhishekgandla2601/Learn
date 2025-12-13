# *args = allows you to pass multiple non-keyword arguments -- stores in tuple
# **kwargs = allows you to pass multiple keyword arguments  -- stores in dictionary
from functools import total_ordering


# * unpacking operator
#   1.positional, 2.default, 3.keyword, 4.Arbitary=combination of both

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1))
#
# def display_name(*args):
#      for arg in args:
#          print(arg, end=" ")
# display_name()
#
#
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_address(street="123 Fake St.",
#               city="Detroit",
#               state="MI",
#               zip="54321")






# *args and **kwargs together

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt = "100",
               city="Detroit",
               state="MI",
               zip="54321")