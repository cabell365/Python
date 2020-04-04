# Python Lists
# A Python List is an ordered collection that can be modified.
# Lists also add duplicate values.
# A list is a type of Array. All programming languages support arrays.
# Below is not every way to manipulate a list but a list of the most popular.

# Define a list
# This list contains a list of strings
my_list_strings = ["this", "is", "a","test"]

# List of integers
my_list_int = [4 , 3, 2 , 1]

# Define an empty list and append to it.
my_test_list = []
print("Empty List:")
print (my_test_list)

# Adding blank line for formatting
print("\n")

my_test_list.append("Hello")
print("Item appended to a list:")
print (my_test_list)

# Adding blank line for formatting
print("\n")

# use a "for" loop with a print list of items (elements)
print("Loop through items in a List:")
for my_string in my_list_strings:
    print (my_string, end = " ")

# Adding blank line for formatting
print("\n")

# print the index and each member of the list using the index method()
print("Loop through items in the List and print the items using the index() method:")
for my_string in my_list_strings:
    print(my_list_strings.index(my_string),my_string, end = " ")

# Adding blank line for formatting
print("\n")

# Use a "for" loop with a read list of strings
print("For loop to read the list:")
for my_int in my_list_int:
    print (my_int, end = " ")

# Adding blank line for formatting
print("\n")

# Get the length of th list
print("Print the length of the List:")
print (len(my_list_strings))

# Adding blank line for formatting
print("\n")

# Use range with len in for loop
print("Use range loop to print the List:")
for my_string_index in range(len(my_list_strings)):
    print(my_list_strings[my_string_index],end = " ")

# Adding blank line for formatting
print("\n")

# print the the List (Defintition of the list)
print("Print the Lists")
print(my_list_strings)
print(my_list_int)

# Adding blank line for formatting
print("\n")

# Print last entry in the list
print("Print last entry in a List:")
print(my_list_strings[-1])

# Print a particular member using an index
# Yoiu can search for the index using the index() method
print("Multiple ways to identify and print an item in a List:")
index_2 = my_list_strings.index("is")
print(my_list_strings[index_2])
print(my_list_strings[1])

# Adding blank line for formatting
print("\n")

# print using a start and end index
print("Print a List item using a start and end index")
print(my_list_strings[1:2])

# Adding blank line for formatting
print("\n")

# Print items in the list up to the end index
print("Print items in the List up to the end index:")
print(my_list_strings[:2])

# Adding blank line for formatting
print("\n")

# Create a new List to another list
print("Create a new List to another List")
my_new_list_string = my_list_strings
for my_new_string in my_new_list_string:
    print (my_new_string, end = " ")

# Adding blank line for formatting
print("\n")

# Create a new List from the subset of a list 
print("Create a new List from the subset of a List:")
my_sub_list_string = my_list_strings[:2]
for my_sub_string in my_sub_list_string:
    print (my_sub_string, end = " ")

# Adding blank line for formatting
print("\n")

# Change Item Value
print("Change an item in a List:")
my_list_strings[1] = "was"
print (my_list_strings)

# Adding blank line for formatting
print("\n")

# Check if an item exists in the list
print("Check if an item exists in a List:")
if "test" in my_list_strings:
    print("The word exists in the List.")

# Adding blank line for formatting
print("\n")

# Add item to the list
print("Add item from a List:")
my_list_strings.append("today")
print(my_list_strings)

# Adding blank line for formatting
print("\n")

# Remove an item from a list
print("Remove item from a List:")
my_list_strings.remove("today")
print(my_list_strings)

# Adding blank line for formatting
print("\n")

# Reverse a list
print("Reverse the order of a List:")
my_list_strings.reverse()
print(my_list_strings)

# Adding blank line for formatting
print("\n")

# Sort a list
print("Sort a List:")
my_list_strings.sort()
print(my_list_strings)

# Adding blank line for formatting
print("\n")

# Insert into  a list
print("Insert into a List:")
my_list_strings.insert(2,"new")
print(my_list_strings)

# Adding blank line for formatting
print("\n")

# Clear the whole list
print("Clear (remove) all items from a List:")
my_list_strings.clear()
print(my_list_strings)

