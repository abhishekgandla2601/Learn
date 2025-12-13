# collection - single "variable" ised to store multiple values
#   List    = [] ordered and changeable. Duplicates OK

#   Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates

#   Tuple   = () ordered  and  unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# # print(fruits[4])#
# print(fruits[0::1])
# # print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# for fruit in fruits:
#     print(fruit)
#
# print("apple" in fruits)
#
# fruits[0] ="pineapple"
# for fruit in fruits:
#     print(fruit)
#
# fruits.append("Grapes")
# print(fruits)
#
# fruits.index("black berry")
# print(fruits)
#
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.clear()
print(fruits)
print(fruits.count("banana"))

fruits.remove("banana")
print(fruits)
fruits.pop(0)
print(fruits)
fruits.pop()# removes at last of the index
print(fruits)
