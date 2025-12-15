# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived:\t"))
# there are 365 days in a year, 24 hours in a day, 60 minutes in an hour and 60 seconds in a minute
seconds_lived = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds")