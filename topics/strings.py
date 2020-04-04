# Strings
# Strings can be parsed by using the method below
# <string>[start:end] where start and end are referred to as indexes
# The default starting index is 0.

# My test string
my_string = "This is a test"

# Parse the first three characters of the string
print (my_string[0:3])

# Parse the "a" from the string
print (my_string[8:9])

# Parse the "is" from the string
print (my_string[5:7])

# Parse the word "test" from the string
print (my_string[10:14])

# print the length (number of character) for the string
print(len(my_string))

# Parse the word "test" from the string using "len" function
print (my_string[10:len(my_string)])

# Parse the word "test" from the string.
# Python ignores the actual index and
# prints until the end of the string
print (my_string[10:100])

# print everything but the last character
# Python starts at the first character of the string
# if the start index is omitting
print(my_string[:-1])

# prints everything after the start index until the end of the string
print(my_string[5:])
