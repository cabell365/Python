# define range max
# Python variables store values in memory
my_range_max = 10

# for loop
for x in range(my_range_max):
    print (x, end=" ")

print()

# For with a specific start of the range
my_start = 4
my_end = 16
for x in range(my_start, my_end):
  print(x, end=" ")

print()

# for loop with a list
mylist = ["this", "is", "a", "test" ]
for myword in mylist:
    print (myword, end=" ")

print()

# Nested loop
for x in range(my_range_max):
    for y in range(my_range_max):
        print (x,y, end=" ")
    
