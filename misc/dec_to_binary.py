# My Number and temp number to do calculations
my_num = 0
my_temp_num = my_num
print ("My number is {}.".format(my_num))

# Dictionary containing decimal and binary numbers
my_binary_list = {128 : 1, 64: 1, 32: 1, 16: 1, 8: 1, 4: 1, 2: 1, 1: 1}

# Default value to hold binary number
my_calc_binary_num = ""

# Read keys in order and find first value less than my_num
# If keys match, use value "1" else use "0"
for keys in my_binary_list.keys():
    if keys <= my_temp_num:
        my_calc_binary_num = my_calc_binary_num + str(my_binary_list[keys])
        my_temp_num = my_temp_num - keys
    else:
        my_calc_binary_num = my_calc_binary_num + "0"

print ("The binary representation for my number {} is {}.".format(my_num, my_calc_binary_num))

# Default counters
my_cnt = 0
my_calc_num = 0

# Convert values and keys to lists
my_list_values = list(my_binary_list.values())
my_list_keys = list(my_binary_list.keys())

# read the binary number\
# if binary number eauals a value then get the key values
# add key values to calulate number
for bit in my_calc_binary_num:
    if str(my_list_values[my_cnt]) == bit:
        my_calc_num = my_calc_num + my_list_keys[my_cnt]
    my_cnt+=1
 
print ("I converted the binary representation {} for my number {} back to {}.".format(my_calc_binary_num,my_num, my_calc_num));

