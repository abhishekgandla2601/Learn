# Create a student dictionary 
# and add 
# first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': "Gandla",
    'last_name':"Abhishek",
    'gender': "M",
    'age':  24,
    'marital_status': "S",
    'skills': "Python",
    'country': "India",
    'city': "Hyderabad",
    'address': "Hyderabad, India"
}
# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills']= ['Python', 'JavaScript', 'C++']
print(student['skills'])

# Get the dictionary keys as a list
print(list(student.keys()))

# Get the dictionary values as a list
print(list(student.values()))

# Change the dictionary to a list of tuples using items() method
print(list(student.items()))

# Delete one of the items in the dictionary
del student['marital_status']
print(student)

# Delete one of the dictionaries
del student

print(student) # This will raise an error since the dictionary has been deleted