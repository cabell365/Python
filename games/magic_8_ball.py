# Magic 8 Ball
# Game created bases on this wikipedia link: https://en.wikipedia.org/wiki/Magic_8-Ball
from random import randint

def get_answers():

    # List of possible answers
    possible_answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
    ]
    
    return(possible_answers)
    
def print_greeting():
    print ("Shake the magic 8 ball and ask your most important question!\n")

def get_the_ball():
    
    magic_8_ball = " ---\n" + "/ 8 \\\n" + "\   /\n" + " ---"
    return magic_8_ball
    
def main():
    
    #Set the continue playing flag to true 
    continue_playing = True
    
    while continue_playing:
        
        # print the greeting to the user
        print_greeting()

        # print out the magic 8 ball
        magic_8_ball=get_the_ball()
        print("{}\n".format(magic_8_ball))
 
        # Prompt the user to ask the question
        my_question=input("Please ask a yes or no question and the magic 8 ball will tell you the future!: ")
 
        # Get the list of possible answers
        my_possible_answers=get_answers()
  
        # Get a randon index from the list
        my_possible_answer_index=randint(0,len(my_possible_answers)-1)

        # Use the index to print the answer
        print(my_possible_answers[my_possible_answer_index])
        
        my_end_selection=input('Do you want to (q)uit? Press any key to continue: ')
        if my_end_selection.lower() == 'q':
            continue_playing=False
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    

