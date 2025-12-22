# dictionaries:
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

empty_dict = {}
print(empty_dict)

dct = {'key1': 'value1', 'key2': "value2", "key3": "value3", "key4": "value4"}
print(len(dct))

# accessing dictionary items
print(dct['key1'])
print(dct['key2'])

# adding items to a dictionary
dct['key5'] = 'value5'
print(dct['key5'])

# adding Items to a Dictionary

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key5'] = 'value5'
print(dct['key5'])

# modifying items in a dictionary
dct['key1'] = 'value-one'
print(dct)

# checking keys in a dictionary
print('key2' in dct)
print('key5' in dct)

# removing key and value pairs from a dictionary
dct.pop('key1')
print(dct)
dct.popitem()
print(dct)
del dct['key2']

print(dct)

# changing dictionary to a list of items
dct = {'key1': 'value1', 'key2':'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())


# this file ended up in a stage where It cannot continue