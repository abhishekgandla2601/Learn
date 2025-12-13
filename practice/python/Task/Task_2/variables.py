firstname = "Gandla"
print(firstname, "Type is :", type(firstname))

lastname = "Abhishek"
print(lastname, "Type is :", type(lastname))

fullname = "Gandla Abhishek"
print(fullname, "Type is :", type(fullname))

country = "India"
print(country, "Type is :", type(country))

city = "Hyderabad"
print(city, "Type is :", type(city))

age = 23
print(age, "Type is :", type(age))

year = 2025
print(year, "Type is :", type(year))

is_married = False
print(is_married, "Type is :", type(is_married))

is_true = True
print(is_true, "Type is :", type(is_true))

is_light_on = True
print(is_light_on, "Type is :", type(is_light_on))

# declare multiple variables on one line
a,b,c = 5,10,15
print(a,b,c)
print("Types of a,b,c are :", type(a), type(b), type(c))


# finding the length of firstname
print("Length of the firstname is :", len(firstname))
print("Length of the lastname is :", len(lastname))

print(firstname > lastname) # firstname is greater than lastname
print(firstname < lastname) 

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
print("The total of num_one and num_two is :", total)
print("The difference between num_one and num_two is :", diff)
print("The product of num_one and num_two is :", product)
print("The division of num_one and num_two is :", division)
print("The remainder of num_one and num_two is :", remainder)