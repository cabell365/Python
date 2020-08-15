#
# Description of the project:
#

# Acme company requires a way for indivdual employees to use passwords for various company applications.
# The company asked the IT team to create a script that employees could use to generate their own passwords.

# The IT team provided two methods for generating passwords:
# * The first method accpets a pass phrase, modifies the characters and returns a password based on the phrase
# * The second password generator generates a 15 character random password

# Company policy states the following:
# * All passwords must be at least 15 characters
# * Any invalid characters used in the pass phrase are replaced with "!"
# * A random special character is placed at the end of the pass phrase
# * Pass phrase should include random use of upper and lower case characters
# * Replace any spaces in the pass pharase with the "_" character
#

from random import randint

class GenPassword:

    # Dictionary used to replace certain letters with numbers
    pass_dict = {"a":"4", "b":"8", "e":"3", "i":"1", "o":"0", "s":"5"}

    # List of special characters for the phrase based passwords
    special_char_list = ["!","@","$","*","=","#"]
    
    # List of invalid password characters using their ascii value
    # Ascii codes can be found here: https://www.ascii-code.com/
    invalid_ascii_int = [37,39,46,47,58,59,62,92,94,96,123,124,125]

    # Minimum length for a password
    min_pass_length = 15

    # Default variables
    my_password_name = ''
    my_rand_num = 0
    my_cnt = 0
    my_cnt2 = 0
    my_upper_interval = 2
    new_char = ''
    
    # ascii value range
    min_ascii_int = 33
    max_ascii_int = 126

    # Define initial method
    def __init__(self, pass_phrase = None):
        if pass_phrase != None:
            self.__pass_phrase = pass_phrase

    # Define getter
    def get(self):
        return self.__pass_phrase

    # Defime setter
    def set(self, pass_phrase):
        self.__pass_phrase = pass_phrase     

    # Method to generate a password based on a phrase 
    def gen_phrase_password(self):
       
        # Read each character of the string in a loop
        for char in self.__pass_phrase:
             
            # If the character matches the key in the dictionary, then concatenate the value from the dictionary
            # Script supports upper and lower case characters using the string lower() method
            if char.lower() in self.pass_dict:
                self.my_password_name = self.my_password_name + self.pass_dict[char.lower()]
                                       
            # else if space then concatenate the "_" character
            elif char == " ":
                self.my_password_name = self.my_password_name + "_"
 
            # else replace any invalid characters with "!"
            elif ord(char) in self.invalid_ascii_int:
                self.my_password_name = self.my_password_name + "!"
 
            # else just concatenate the character from the loop
            else:
                
                # Every 2nd character convert character to upper and reset counter
                if self.my_cnt == self.my_upper_interval:
                    self.new_char = char.upper()
                    self.my_cnt = 0
                else:
                    self.new_char = char
                    
                self.my_password_name = self.my_password_name + self.new_char
                     
                # increment counter
                self.my_cnt+=1
                
        # Generate random number
        self.my_rand_num = (randint(0, len(self.special_char_list)-1))                         
            
        # Get a special character based on random number and concatenante to end of password
        self.my_password_name = self.my_password_name + self.special_char_list[self.my_rand_num]
            
        # return the password
        return self.my_password_name
 
    # Method to generate a random password
    def gen_ascii_password(self):
        
        # While the counter is les than minimum password length
        while self.my_cnt2 < (self.min_pass_length):
            
            # Generate a random number to represent the ascii value of a character
            self.my_chr_int = randint(self.min_ascii_int,self.max_ascii_int)
            
            # If random ascii value is not in the invalid character list, use to create password.
            if self.my_chr_int not in self.invalid_ascii_int:
                
                # Get a character based on a random generated ascii value
                self.my_password_name = self.my_password_name + (chr(self.my_chr_int))
                
                # increment counter because we found a valid character for password
                self.my_cnt2+=1

        # return the password
        return self.my_password_name

    # Check length of pass phrase
    def is_pass_phrase_len_valid(self):
        if len(self.__pass_phrase) < self.min_pass_length:
            return False
        else:
            return True

#
# Start of creating objects
#

# Phrase based Password

# Test 1: Verify creation of a password
# Company policy is all passwords must be 15 characters.
# We perform the check prior to generating a password using class property
print("Test 1: Verify creation of a password:")
my_pass_phrase = "The desert is great"
print("The password phrase selected: {}".format(my_pass_phrase))
MyPhrasePassword = GenPassword(my_pass_phrase)
if len(my_pass_phrase) > MyPhrasePassword.min_pass_length:
    my_phrase_password = MyPhrasePassword.gen_phrase_password()
    print("Pass phrase is valid.")
    print("Generated Password: {}".format(my_phrase_password))
else:
    print("Pass phrase is too short!")

print("\n")

# Test 2:  Attempt to create password that is two short.
# Company policy is all passwords must be 15 characters.
# We perform the check prior to generating a password using class property
print("Test 2: Attempt to create a password that is two short:")
my_pass_phrase = "The desert"
print("The password selected: {}".format(my_pass_phrase))
MyPhrasePassword2 = GenPassword(my_pass_phrase)
if len(my_pass_phrase) > MyPhrasePassword2.min_pass_length:
    my_phrase_password = MyPhrasePassword2.gen_phrase_password()
    print("Pass phrase is valid.")
    print("Generated Password: {}".format(my_phrase_password))
else:
    print("Pass phrase is too short!")

print("\n")

# Test 3:  Create another password using the setter on the same object
# Company policy is all passwords must be 15 characters.
# We use our method this time to check the length of the pass phrase
print("Test 3: Use method to validate pass phrase length:")
my_pass_phrase = "I am tired"
print("The password phrase selected: {}".format(my_pass_phrase))
MyPhrasePassword2 = GenPassword()
MyPhrasePassword2.set(my_pass_phrase)
if MyPhrasePassword2.is_pass_phrase_len_valid():
    my_phrase_password = MyPhrasePassword2.gen_phrase_password()
    print("Pass phrase is valid.")
    print("Generated Password: {}".format(my_phrase_password))
else:
    print("Pass phrase is too short!")

print("\n")

# Test 4:  Create password based on a phrase with an invalid character
# Rule is to change invalid characters to "!"
print("Test 4: Create password containing an invalid character:")
my_pass_phrase = "The desert is great %"
print("The password phrase selected: {}".format(my_pass_phrase))
MyPhrasePassword2 = GenPassword(my_pass_phrase)
if len(my_pass_phrase) > MyPhrasePassword2.min_pass_length:
    my_phrase_password = MyPhrasePassword2.gen_phrase_password()
    print("Pass phrase is valid.")
    print("Generated Password: {}".format(my_phrase_password))
else:
    print("Pass phrase is too short!")

print("\n")

# Test 5:  Create another password using the setter on the same object
# Company policy is all passwords must be 15 characters.
# We use our method this time to check the length of the pass phrase
print("Test 5: Use setter to create password using same object with new phrase:")
my_pass_phrase = "I am tired of winter weather"
MyPhrasePassword2 = GenPassword()
MyPhrasePassword2.set(my_pass_phrase)
if MyPhrasePassword2.is_pass_phrase_len_valid():
    my_phrase_password = MyPhrasePassword2.gen_phrase_password()
    print("Pass phrase is valid.")
    print("Generated Password: {}".format(my_phrase_password))
else:
    print("Pass phrase is too short!")

print("\n")

# Test 6: Generate random password
print("Test 5: Generate random password:")
MyAsciiPassword = GenPassword()
my_ascii_password = MyAsciiPassword.gen_ascii_password()
print(my_ascii_password)

print("\n")

# Test 7: Generate another random password
print("Test 6: Generate another random password:")
MyAsciiPassword2 = GenPassword()
my_ascii_password = MyAsciiPassword2.gen_ascii_password()
print(my_ascii_password)

