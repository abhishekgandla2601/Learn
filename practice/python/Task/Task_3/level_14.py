# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter Hours:\t\t"))
r_p_p = int(input("Enter Rate per Hour:\t"))
earnings = hours * r_p_p
print(f"Your weekly earning is: {earnings:.2f}")