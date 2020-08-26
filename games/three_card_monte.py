# Three Card Monte Game
# This is a basic three card monte game
# The objective of the game is to find the ace of diamonds (A-D) among 3 cards.
#
# The game sorts three cards:
# * A-D (Ace of Diamonds)
# * A-C (Ace of Clubs)
# * A-S (Ace of Spades)
#
# You must select the location based on the following:
# * 0 for first slot
# * 1 for middle slot
# * 2 for last slot
#

from random import randint

# Function containing cards
def get_cards():
    the_cards = ["A-D","A-S","A-C"]
    
    return the_cards

def shuffle_cards(the_cards):
    
    random_index=randint (0,len(the_cards)-1)
    temp_card=the_cards[random_index]
    
    # Remove card from list
    the_cards.remove(temp_card)

    # Add card to back of the list
    # Reinsert the value in the list
    the_cards.insert(len(the_cards)+1, temp_card)

    # Return the new card list
    return the_cards
    
def main():

    # Counter and max value
    shuffle_cnt=0
    num_wins=0
    num_losses=0
    games_played=0
    max_shuffles = 5000

    # valid selection
    valid_selections=[0,1,2]
    
    # The winning card
    winning_card="A-D"

    # Flags
    is_not_valid_selection=True
    continue_playing=True

    # Randomly show cards when counter equals these values
    show_cards = [27,36,109,4000]

    while continue_playing:
        while is_not_valid_selection:
            
            # Get initial cards
            my_cards = get_cards()
            print("To win you need to find the Ace of Diamonds (A-D)\n")
            print("Here are the three cards:")
            print("%s\n" % my_cards)
        
            # Shuffle cards
            print("Shuffling the deck {} times...\n".format(max_shuffles))
            while shuffle_cnt < max_shuffles:
                my_shuffled_cards=shuffle_cards(my_cards)
                if shuffle_cnt in show_cards:
                    print("Random sneak peek: shuffle number: {}".format(shuffle_cnt))
                    print("%s\n" % my_shuffled_cards)
                shuffle_cnt+=1

            shuffle_cnt=0
            
            print ("Where is the Ace of Diamonds (A-D)?")
            my_selection=input('Please input location of the A-D (0 for first slot, 1 for middle slot, 2 for last slot: ')
            if my_selection:
                if my_selection.isdecimal():
                    my_selection_int=int(my_selection)
                    if my_selection_int in valid_selections:
                        # Final location of the card
                        if my_shuffled_cards[my_selection_int] == winning_card:
                            print("\nYou Win!\n")
                            num_wins+=1
                        else:
                            print("\nSorry, wrong choice.\n")
                            num_losses+=1
                    
                        print("Here are the cards: \n{} \n".format(my_shuffled_cards))
                        games_played+=1
        
                        my_end_selection=input('Do you want to (q)uit? Press any key to continue: ')
                        if my_end_selection.lower() == 'q':
                            is_not_valid_selection=False
                            continue_playing=False
                        else:
                            is_not_valid_selection=True

    print("\nYour Stats:")
    print("----------------------------")
    print("Number of Games: {}".format(games_played))
    print("Number of winners: {}".format(num_wins))
    print("Number of losses: {}".format(num_losses))
    
# Execute main program
if __name__== "__main__":
    main()
    

    
