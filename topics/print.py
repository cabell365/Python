# Print Statement Basics

name1 = "Steve"
name2 = "Jeff"
name3 = "Lisa"

# No formating
print ("The students are named", name1, name2, "and", name3,".")

# Formatted print statement
print ("The students are named %s, %s and %s." % ( name1, name2, name3))

# Formatted with the new line value added
print ("The students are named: \n%s\n%s\n%s" % ( name1, name2, name3))

# Basic printing of a string
# Single and double quotes both work
print("This is a test")
print('This is a test')

# print a variable storing a string
my_str = "This is a test"
print(my_str)

# Format a string variable
my_str = "This is a test"
print("%s" % my_str)

This is a test

# Anothwer example of formating a string variable
my_str2 = "Craig"
print("My name is %s" % my_str2)

# Another way to format a string
my_str = "Craig"
print("{}".format(my_str))

# Format a value as both an int and a string
my_int = 27
print(my_int)
print("My favorite number is %d" % my_int)
print("My favorite number is %s" % my_int)

# Several ways to format and print a string
# Feel free to play aroung with the code to
# learn how it works.
my_name = "Craig"
print('{:10}Bell'.format(my_name))
print('{:^10}'.format(my_name))
print('{:>10}'.format('test123'))
print('{:^4}'.format('zip'))
read_until = 3
print('{:.{}}'.format('xylophone', read_until))
print('{:f}'.format(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
