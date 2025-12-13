# if = Do some code only if some condition is True
# Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print(f"Your age is {age}, You are now signed up!")
elif age<0:
    print("You haven't been born yet!")
else:
      print("Your age must be 18+ to sign up!")
