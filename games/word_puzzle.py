from random import randint

# Use a random number to select the puzzle
def select_puzzle():
    available_puzzles = ["let it ride", \
                         "what you see is what you get", \
                         "love and happiness", \
                         "born to be wild", \
                         "everybody loves the sunshine", \
                         "you fake the funk, your nose got to grow", \
                         "seasons don't fear the reaper", \
                         "what the world needs now is love, sweet love",
                         "one world is enough for all of us",
                         "don't believe the hype"]
    
    puzzle_selected = randint(0,len(available_puzzles)-1)
    return available_puzzles[puzzle_selected]

# Build a list containing eash character in the puzzle
def build_puzzle(puzzle_sentence):   
    puzzle_list = []
    for letter in puzzle_sentence:
        puzzle_list.append(letter)
    return puzzle_list

# Build index matching puzzle. 1 equals letter found. 0 equal not found
def build_puzzle_index(puzzle_list):
    special_char_list = ["!",",","'"," "]
    puzzle_index_list = []
    for letter in puzzle_list:
        if letter in special_char_list:
            puzzle_index_list.append(1)
        else:
            puzzle_index_list.append(0)    
    return puzzle_index_list

# Return a random $ amount between 0 and 100
def spin_wheel():
    wheel_dollar_amounts = [0,10,20,30,40,50,60,70,80,90,100]
    amount_index = randint (0,len(wheel_dollar_amounts)-1)
    return wheel_dollar_amounts[amount_index]

# Guess a letter from the puzzle
def guess_letter(letter,puzzle_list,puzzle_index_list):
    letter_index = 0
    letters_found_list = []
    for letters in puzzle_list:
        if (puzzle_list[puzzle_list.index(letters)]) == letter:
            puzzle_index_list[letter_index] = 1
            letters_found_list.append(letter_index)
        letter_index+=1
    return puzzle_index_list, len(letters_found_list)

# print the current state of the puzzle.
def print_current_puzzle(puzzle_list, puzzle_index_list):
    index_cnt = 0
    current_puzzle = ""
    for letter_found in puzzle_index_list:
        if letter_found == 1:
            current_puzzle = current_puzzle + puzzle_list[index_cnt]
        else:
            current_puzzle = current_puzzle + "*"
        index_cnt+=1
    return current_puzzle
   
# Determine if the puzzle is solved or not
def is_puzzle_not_solved(puzzle_index_list):
    if 0 in puzzle_index_list:
        unsolved_flag = True
    else:
        unsolved_flag = False
    return unsolved_flag

# Print the rules of the game.
def print_rules():
    print("\n------------------------------------------------------------------------------")
    print("The script is a simple 'wheel of fortune' type of game.")
    print("There are random puzzles to solve by guessing letters.")
    print("All letters are converted to lower case and all puzzles are in lower case.")
    print("Vowels are selected like consonants.")
    print("The wheel contains dollar amounts in increments of 10 from 0 to 100.")
    print("I am generous. You are not penalized for incorrect choices.")
    print("You only receive $ on correct answers")
    print("The bankruptcy value does not exist but zero does. You can guess on zero but do not receive $.")
    print("You can exit at anytime by terminating the program with Ctrl C")
    print("Lets play our word game!")
    print("-------------------------------------------------------------------------------")

# Start of the main program
def main():

    # Print rules to the game
    print_rules()

    # Select a puzzle
    my_selected_puzzle = select_puzzle()
    # print(my_selected_puzzle)

    # Bulld list to hold letters in the puzzle
    my_puzzle_list = build_puzzle(my_selected_puzzle)
    #print (my_puzzle_list)

    # Build index to determine which letters are found
    my_puzzle_index_list = build_puzzle_index(my_puzzle_list)
    #print(my_puzzle_index_list)

    # Defau;t variables
    my_total_guesses = 0
    my_earnings = 0
    my_wheel_money = 0
    my_unsolved_flag = True
    my_current_puzzle = ""
    letters_chosen_list = []

    # stay in loop until puzzle is solved.
    while my_unsolved_flag:

        print ("Letters chosen so far:")
        for letters_chosen in letters_chosen_list:
            print(letters_chosen,end=" ")
        print("\n")
     
        my_letters_found = 0
        print("Current earnings: ${}".format(my_earnings))
        my_current_puzzle = print_current_puzzle(my_puzzle_list, my_puzzle_index_list)
        print("Current puzzle: {}".format(my_current_puzzle))
        
        print("\nSpin the wheel!")
        my_wheel_money = spin_wheel()
        
        print("You landed on ${}\n".format(my_wheel_money))

        my_letter=input("Please select a letter: ")
        letters_chosen_list.append(my_letter)
        
        my_puzzle_index_list, my_letters_found = guess_letter(my_letter.lower(),my_puzzle_list,my_puzzle_index_list)
        my_earnings = my_earnings + (my_wheel_money * my_letters_found)
        print("Number of {}'s found in the puzzle: {}".format(my_letter, my_letters_found))
        print("-------------------------------------------------------------------------------")
        
        my_unsolved_flag = is_puzzle_not_solved(my_puzzle_index_list)
        my_total_guesses+=1

    print("\nStats")
    print("-------------------------------------------------------------------------------")
    print("Number of characters in puzzle (including spaces and special characters): {}".format(len(my_selected_puzzle)))
    print("Total number of guesses: {}".format(my_total_guesses))
    print("The answer to the puzzle: {}".format(my_selected_puzzle))
    print("Total winnings: ${}".format(my_earnings))

# Execute main program
if __name__== "__main__":
    main()
