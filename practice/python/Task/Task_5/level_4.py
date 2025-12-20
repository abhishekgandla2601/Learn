# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()

print(it_companies)

print("The number of companies: ", len(it_companies))

# Print the first, middle and last company

print("First_company: ", it_companies[0])

middle_company = len(it_companies) // 2

print("Middle_company: ", it_companies[middle_company])

print("Last_company: ", it_companies[-1])

# Print the list after modifying one of the companies

it_companies.insert(1, "Meta")
print(it_companies)

# Add an IT company to it_companies

it_companies.append("ZOHO")

print(it_companies)

# Insert an IT company in the middle of the companies list

new_middle = len(it_companies) // 2
print(new_middle)

it_companies.insert(4, "RS_technologies")
print(it_companies)

# Change one of the it_companies names to uppercase 

print(it_companies[2].upper())

print("Google" in it_companies )

it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# print(it_companies + "#")
# list can be concatenated with list 

# Slice out the first 3 companies from the list

print(it_companies[0:3]) # first 3 companies from the list

# Slice out the last 3 companies from the list
print(it_companies[-3:])


# Slice out the middle IT company or companies from the list
print(len(it_companies)//2)
print(it_companies[5])# middle IT company

# remove the first IT company from the list 
