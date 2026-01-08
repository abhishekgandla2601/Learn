# dictionary
D1 = {}
print(type(D1))

D2 = {'pid': 1001, 'pname':"mobile_1", 'price': 23000.0}
print(D2)

# keys()

for x1 in D2.keys():
    print(x1)
    
# values()
for x2 in D2.values():
    print(x2)

# items()
for x3 in D2.items():
    print(x3)# gives in tuple format
    print(type(x3))
print(D2)
# popitem()
D2.popitem()
print(D2)

d3 = D2.get('pname')
print(d3)

# update()
D4 = dict()
print(D4)
D4.update({"Pid":1001,"Pname":"Mobile_1","Price":21000})
print(D4)