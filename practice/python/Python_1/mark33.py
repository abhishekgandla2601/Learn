# f-strings in python

letter = "Hey my name is {} and I am from {}"

country = "India"

name = "Abhishek"

print(letter.format(name, country))
print(letter.format(country, name))

# it gets reverse to make this work

letter1 = "Hey my name is {0} and I am from {1}"
country1 = "India"
name1 = "Abhishek"
print(letter.format(name1, country1))
print(f"Hey my name is {name1} and I am from {country1}")

txt = "For only {price:.2f} dollars!"# to take 2 decimal places
print(txt.format(price = 49.099999))


cost = 59.093848

txt1 = f"For only {cost:.2f} dollars!"

print(txt1)

print(type(f"{2 * 30}"))