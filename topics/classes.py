# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes (properties) attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.
#
# self represents the instance of the class. By using the “self” keyword
#   we can access the attributes and methods of the class in Python.
#
# The __init__, get, set and print are standard methods you should always add to classes.
# Interaction with an object should always be through methods
# It is also customary to add the prefix "__" to the object (self) variable 

#
# simple class that has a string as a property
#
class Word:
    
    def __init__(self, word):
        self.__word = word
    
    def get(self):
        return self.__word
    
    def set(self,word):
        self.__word = word
    
    def print(self):
        print(self.__word)

# Define string variable
my_word = "Today"

print("MyWord is the object and Word is the Class")
print("Instantiate object by setting the class property word and execute print() method:")
MyWord = Word(my_word)
MyWord.print()
print("\n")

print("Get value for class property word using the get() method and print the returned value:")
my_get_word = MyWord.get()
print(my_get_word)
print("\n")

print("Set the value for the class property word using the set() method and print the returned value:")
my_new_word = "Tomorrow"
MyWord.set(my_new_word)
my_get_set_word = MyWord.get()
print(my_get_set_word)
MyWord.print()
print("\n")

# Multiple objects can be created from a class
print("Multiple objects can be created from a class:")
MyWord2 = Word("Python")
MyWord2.print()
print("\n")

#
# Define the class for a list of students
#
class Students:
    
    def __init__(self, student_list):
        self.__student1 = student_list[0]
        self.__student2 = student_list[1]
        self.__student3 = student_list[2]
        
    def get(self):
        student_list = [self.__student1,self.__student2,self.__student3]
        return student_list

    def set(self,student_list):
        self.__student1 = student_list[0]
        self.__student2 = student_list[1]
        self.__student3 = student_list[2]

    def print(self):
        print (self.__student1, self.__student2, self.__student3)
        
# Create a Python List for student names
my_student_list = ["Jennifer", "Andrew", "Craig"]

# Instantiate my object for the class Students using the __init__ method")
MyStudents = Students(my_student_list)

# Execute the print method to display the students.
print("Execute the print method to display the students:")
MyStudents.print()
print("\n")

# Use the get() method to get the properties(attributes)
print("Use the get() method to get the properties(attributes):")
my_student_list = MyStudents.get()
for my_student in my_student_list:
    print(my_student,end=" ")
print("\n")

# Use the set method to changet the values
print("Use the set method to changet the values:")
my_new_student_list = ["Lynn","Christian","Andrew"]
MyStudents.set(my_new_student_list)
MyStudents.print()
print("\n")

# A class with integers 
class Numbers:

    # Class variable. Is usually a constant
    class_num = 5
        
    def __init__(self, num):
        self.__num = num

    def get(self):
        return self.__num

    def set(self,num):
        self.__num = num
        
    def double_num(self):
        return self.__num * self.__num
           
    def is_number_odd_even(self):
        if self.__num % 2 == 0:
            num_type = "Even"
        else:
            num_type = "Odd"
        return num_type
    
    def triple_num(self):
        return self.__num * self.__num * self.__num
    
    def num_times_class_var(self):
        return self.__num * self.class_num

    def print(self):
        print (self.__num, self.class_num)
        
# Define an integer variable
my_num = 9

# Instantiate my object for the class Numbers using the __init__ method
MyNumbers = Numbers(my_num)

print("Use get() method to get the value of num for the objects:")
my_num_get = MyNumbers.get()
print(my_num_get)
print("\n")

# print class property
print("Print class property:")
print(MyNumbers.class_num)
print("\n")

# Execute print method
print("Execute the print method:")
MyNumbers.print()
print("\n")

# Execute method and print value
print("Execute the double_num() method and print the value returned:")
my_double_num = MyNumbers.double_num()
print(my_double_num)
print("\n")

# Execute method and print value
print("Execute the is_number_odd_even() method and print the value returned:")
my_num_type = MyNumbers.is_number_odd_even()
print(my_num_type)
print("\n")

# Execute method and print value
print("Execute the triple_num() method and print the value returned:")
my_triple_num = MyNumbers.triple_num()
print (my_triple_num)
print("\n")

# Change the value of a num property
print("Set the value of the num property:")
MyNumbers.set(15)
MyNumbers.print()
my_num_var = MyNumbers.num_times_class_var()
print(my_num_var)
print("\n")

# print the object
print("Print the object:")
print(MyNumbers)
print("\n")

# Delete object and verify it is undefined
# It is usually a good practice to delete objects when they are no longer needed.
# However, Python garbage collection will clean up the memory used by an object.
print("Delete a object and verify it is undefined:")
del MyNumbers
try:
    MyNumbers
except NameError:
    print ("Object undefined")
print("\n")

# Define an empty class
class EmptyClass:
    pass

class Num:
    def __init__(self,num1, num2):
        self.__num1 = num1
        self.__num2 = num2
    
    def compnum(self):
        if self.__num1 > self.__num2:
            return self.__num1
        else:
            return self.__num2

my_num1 = 7
my_num2 = 4
MyNum = Num(my_num1,my_num2)
ret_num = MyNum.compnum()
print (ret_num)






