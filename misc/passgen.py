import string
import random
import sys

def id_generator(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    mypass = id_generator()
    print mypass

# execute main function
if __name__ == "__main__":
    main()

# Exit the program
sys.exit()
