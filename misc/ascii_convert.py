my_word = "wonderful"
print("My word is: {}\n".format(my_word))
      
# Lists to hold ascci values for lower and upper case letters
my_ord_list = []
my_ord_upper_list = []

# Add lower case ascii values to a list
for my_letter in my_word:
    my_ord_list.append(ord(my_letter))

# Add upper case ascii values to a list
for my_upper_letter in my_word.upper():
    my_ord_upper_list.append(ord(my_upper_letter))

print ("Lower case ascii values for {}:".format(my_word))
for my_ord_num in my_ord_list:
    print (my_ord_num, end = " ")

print("\n")

print ("Upper case ascii values for {}:".format(my_word))
for my_ord_upper_num in my_ord_upper_list:
    print (my_ord_upper_num, end = " ")

print("\n")

print ("Convert lower case ascii values back to letters:")
for my_ord_num in my_ord_list:
    print (chr(my_ord_num), end = "")

print("\n")

print ("Convert upper case ascii values back to letters:")
for my_ord_upper_num in my_ord_upper_list:
    print (chr(my_ord_upper_num), end = "")