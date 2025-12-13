# string methods
# string are immutable
a = 'Harry'
print(len(a))
# making uppercase
print(a.upper())
#making lowercase
print(a.lower())

# it means string methods create new string, they wont be changed

#strip
print(a.rstrip("!"))

#replace
print(a.replace("Harry", "John"))

print(a)

#split
print(a.split(" "))

blogHeading = "introduction to js"

print(blogHeading.capitalize())# first character to uppercase and makes all characters to lower case

#center()

str1 = "Welcome to the console"
print(len(str1))

print(len(str1.center(50)))

#count()
print(a.count("Harry"))

#endswith()

print(str1.endswith('!!!'))

str1 = "Welcome to the consloe!!!"
print(str1.endswith("to",4, 10))

#find()
str1 = "He's name is Dan. He is an honest man."

print(str1.find("is"))

#index()
print(str1.index("is"))

#isalnum()

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
#islower()
str1 = "hello world"
print(str1.islower())

#isprintable()

str1 = "We wish you\n"
print(str1)
print(str1.isprintable())

#isspace()

str1 = "            "
print(str1.isspace())#tab

str2 = "       "
print(str2.isspace()) #spacebar

#istitle()
str2 = 'To kill a mocking bird'
print(str2.istitle())

#startswith()

str1 = "Python is a Interpreted Language"
print(str1.startswith('Python'))

#swapcase()
# it converts lower cases to upper and upper case to lower

print(str1.swapcase())

#title()

str1 = "His name is Dan. Dan is an honest man"
print(str1.title())