#
# Script reads a file, encrypts the contents and writes to a file.
# The script also decrypts the encrypted file and displays the message
#
# The encryption is perfoemd by doing the following:
#    * Create a two random 4 digit number and use one as a prefix and the other as a suffix for each character
#    * The letters are converted to upper case and then the decimal ascii value is used
#    * The entire sentence is then reversed
#
# The decryption requires:
#
#    * Reversing the sentence
#    * Parse the sentence into 10 digit numbers and add to a list
#    * Read the list parsing out the two characters between the 2 4 digit random numbers
#    * Convert the 2 digit number (ascii decimal code) back to a letter
#    * Concatenate the letters back together to recreate the sentence


from random import randint
import os.path
from os import path

def encrypt(my_sentence):
    min_rand_int = 1000
    max_rand_int = 9999
    prefix = 0
    suffix = 0
    number_string = ""
    encrypted_sentence = ""
    encrypted_reverse_sentence = ""
    
    for x in my_sentence:
        prefix = str(randint(min_rand_int,max_rand_int))
        suffix = str(randint(min_rand_int,max_rand_int))
        number_string = prefix + str(ord(x.upper())) + suffix
        encrypted_sentence = encrypted_sentence + number_string
        
    encrypted_reverse_sentence = encrypted_sentence[::-1]
    return encrypted_reverse_sentence

def decrypt(encrypted_sentence):
    max_val = 10
    my_letter_list = []
    string_start = 4
    string_end = 6
    letter = ""
    decrypted_sentence = ""

    encrypted_sentence_no_newline = encrypted_sentence.replace("\n","")
    encrypted_sentence_reversed = encrypted_sentence_no_newline[::-1]
    for i in encrypted_sentence_reversed:
        letter = letter + i
        if len(letter) == max_val:
            my_letter_list.append(letter)
            letter = ""

    for encrypted_letter in my_letter_list:
        decrypted_sentence = decrypted_sentence + chr(int(encrypted_letter[string_start:string_end]))
    return (decrypted_sentence)

def main():
    my_file = "message.txt"
    my_encrypted_file = "encrypt_message.txt"
 
    if path.exists(my_file):
        
        fr = open(my_file, "r")
        print ("Original Message:")
        for line in fr:
            print(line)
        fr.close()

        fr2 = open(my_file, "r")
        fw = open(my_encrypted_file, "w")
        for line2 in fr2:
            my_encrypted_sentence = encrypt(line2)
            fw.write(my_encrypted_sentence)
            fw.write("\n")

        fr2.close()
        fw.close()

        print("\n")

        fre = open(my_encrypted_file, "r")
        print ("Encrypted Message:")
        for encrypted_line in fre:
            print(encrypted_line)
        fre.close()

        fr3 = open(my_encrypted_file, "r")
        print ("Decrypted Message:")
        for line3 in fr3:
            my_decrypted_sentence = decrypt(line3)
            print("{}".format(my_decrypted_sentence))
        fr3.close()
    else:
        print("Please create a file named message.txt and enter a typed message in the file to encryot and decrypt!")

# Execute main program
if __name__== "__main__":
    main()


