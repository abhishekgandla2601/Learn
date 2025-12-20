# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))


list(age)
print(len(list(age)))

print("Length of the list and the set: ", len(age) - len(list(age)))

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
print(set(sentence.split()))
for i in sentence:
    print(i, end=",")