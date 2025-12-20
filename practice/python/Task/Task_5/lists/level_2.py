# declare a list with more than five items
my_list = [1, "Abhishek", 23, 25000.00, True, "python"]
print("The list is: ", my_list)

# Find the length of your list
print("\n",len(my_list))  # prints the length of the list 

# Get the first item, the middle item and the last item of the list

first_item = my_list[0]
print("\n first item is: ", first_item)
middle_index = len(my_list) // 2
middle_item = my_list[middle_index]
print("\n middle item is: ", middle_item)
last_item = my_list[-1]
print("\n last item is: ", last_item)

