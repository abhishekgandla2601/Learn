# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: \t"))

if number % 2 ==0:
    print(f"The number {number:.2f} is even.")
else:
    print(f"The number {number:.2f} is not even.")