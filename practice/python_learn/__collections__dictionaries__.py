# dictionary = a collection of {key:value} pairs
#               ordered  and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "INDIA": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital does not exist")
#
# capitals.update({"Germany": "Berlin"})# inserting new key value pair
# capitals.pop("China")
# capitals.popitem()# removes one element
# capitals.clear()
keys = capitals.keys()
values = capitals.values()

print(keys)
print(values)
print(capitals)

for key in capitals.keys():
    print(key)
print()
for value in capitals.values():
    print(value)

items=capitals.items()

print(items)
print()
for key, value in capitals.items():
    print(f"{key}:{value}")