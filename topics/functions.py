# functions
# A function is defined with the keyword "def"

# Very Basic function
# All commands in the function should be indented
def print_hello():
    print ("hello")

# Passing a variable to a function
# The variable passed is a called an argument
def print_hello_var(this_greeting):
    print(this_greeting)

# Functions can be accept multiple arguments
def print_hello_goodbye(this_hello,this_goodbye):
    print(this_hello,this_goodbye)

# Functions can have a default setting
def print_hello_default(this_greeting = "hello"):
    print (this_greeting)

# This function returns a value
# The return keyword returns a value from the function
def get_double (this_num):
    this_double_num = this_num * this_num
    return this_double_num

# The pass keyword allows for an empty function
# This can be used to test calling a function before the commands are ready
# It can also be used when multiple programmers are working on functions
def print_not_ready():
    pass

# Recursive function is a function that calls itself
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

# Functions should be defined at the top of the script and executed below
# A function must be defined before you can call it.
# The open and closed parentheses are required
print_hello()

# The variable is passed by placing it between the parentheses
# The greeting variable here and in the function are different
# The variable in the function is within the scope of the function
greeting = "hello"
print_hello_var(greeting)

my_greeting = "hello"
print_hello_var(my_greeting)

# You can also perform keyword arguments
print_hello_var(this_greeting = "hello")

# Functions can be passed multiple values
hello = "hello"
goodbye = "goodbye"
print_hello_goodbye(hello,goodbye)

# call function without passing a argument
print_hello_default()
new_greeting = "howdy"
print_hello_default(new_greeting)

# Functions can return values
# Functions that return values are often created as "helper" functions
# Numeric (int) variables should be defined or defaulted before using
# # double_num is storing the value returned by the function
num = 9
double_num = 0
double_num = get_double(num)
print(double_num)

# I can now use the returned value later in my script
if double_num == 81:
    print("Found")

# The function will not execute any commands
print_not_ready()

# Calling a recursive function
# NOTE: The function is passed as an argument to the print command
num = 6
print("The factorial of", num, "is", factorial(num))
