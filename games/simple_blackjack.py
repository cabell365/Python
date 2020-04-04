from random import randint

def build_deck():
    deck = []
    suit_list = ["S","H","D","C"]
    face_card_list = ["A","K","Q","J"]
    numbered_card_list = ["2","3","4","5","6","7","8","9","10"]

    for suit in suit_list:
        for face_card in face_card_list:
            face_card_suit = face_card + "-" + suit
            deck.append(face_card_suit)

    for suit in suit_list:
        for numbered_card in numbered_card_list:
            numbered_card_suit = numbered_card + "-" + suit
            deck.append(numbered_card_suit)

    return deck

def get_card(deck):  
    is_not_card_available = True
    while is_not_card_available:
        card_delt = randint (0,len(deck)-1)
        if card_delt < len(deck)-1:
            if deck[card_delt] in deck:
                deck.remove(deck[card_delt])
                is_not_card_available = False
    return deck, deck[card_delt]

def get_card_value(card):
    card_value_dict = {"A":11,"K":10,"Q":10,"J":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
    return card_value_dict[card.split("-",1)[0]]

def print_lines():
    number_of_lines = 100
    print(number_of_lines * "-")
    print("\n")

def print_rules():
    print("This is a simple Blackjack game.")
    print("Player two is the computer")
    print("Here are the basic rules of the game:")
    print("\tThe game currently does not supports splits or double down")
    print("\tThe Ace ('A') is always 11 and not 11 or 1")
    print("\tThe dealer must hit on 16 was not implemented.")
    print("\tThe remaining basic rules of Blackjack apply")
    print("The cards of the deck are represented as the following:")
    print("\tThe deck suits are 'S' for Spades, 'H' for Hearts, 'D' for Diamonds and 'C' for Clubs")
    print("\tThe 'A' is Ace, 'K' is King, 'Q' is Queen and 'J' is Jack")
    print("\tThe non-face cards are represented with the numbers 2 through 10")

# Build the initial deck
my_deck = build_deck()

# Default values
rebuild_deck_value = 10
number_of_hands = 0
player_1_wins = 0
player_2_wins = 0
players_push = 0
continue_game = True
blackjack = 21

# print rules
print_lines()
print_rules()

# Play game until user select anything other than 'y'
while continue_game:

    # Rebuild deck when the number of cards less then rebuild_deck_value
    if len(my_deck) < rebuild_deck_value:
        my_deck = build_deck()

    # Print current totals
    print_lines()
    print("Current Totals:")
    print_lines()
    print("Player 1 wins: {}".format(player_1_wins))
    print("Player 2 wins: {}".format(player_2_wins))
    print("Player Pushes: {}".format(players_push))
    print_lines()
    
    # Default / Reset values
    init_cards_delt = 4
    init_card_delt_cnt = 0
    player_1_list = []
    player_2_list = []
    my_player_1_turn = True
    my_player_2_turn = True
    
    # Deal initial 4 cards
    while init_card_delt_cnt != init_cards_delt:
        my_deck,my_card = get_card(my_deck)
        if init_card_delt_cnt % 2 == 0:
            player_1_list.append(my_card)
        else:
            player_2_list.append(my_card)
       
        init_card_delt_cnt+=1

    print ("player 1's cards:")
    my_total_player_1_card_value = 0
    for player_1_card in player_1_list:
        my_player_1_card_value = get_card_value(player_1_card)
        my_total_player_1_card_value = my_total_player_1_card_value + my_player_1_card_value
        print(player_1_card,end=" ")

    print("\n")
    print("Players 1 total card value is {}".format(my_total_player_1_card_value))
    print("\n")

    print("Player 2's cards:")
    print(player_2_list[0]," ? ", end=" ")
    print("\n")

    # Get value for player 2 cards
    my_total_player_2_card_value = 0
    for player_2_card in player_2_list:
        my_player_2_card_value = get_card_value(player_2_card)
        my_total_player_2_card_value = my_total_player_2_card_value + my_player_2_card_value

    # End game if either player got 21
    if my_total_player_1_card_value == blackjack:
        print("Player 1 got blackjack!")
        my_player_1_turn = False
        my_player_2_turn = False
    elif my_total_player_2_card_value == blackjack:
        print("Player 2 got blackjack!")
        print("Player 2's cards:")
        for player_2_card in player_2_list:
            print(player_2_card,end=" ")
            print("\n")
        my_player_1_turn = False
        my_player_2_turn = False

    # Get value of each card delt for player 1
    while my_player_1_turn:
          
        my_player_1_choice_str=input("Player 1: Please select (h)it or (s)tay:")
        my_player_1_choice_lower = my_player_1_choice_str.lower()
        if my_player_1_choice_lower == "h":
            my_deck,my_card = get_card(my_deck)
            print("Card received: {}".format(my_card))
            player_1_list.append(my_card)
            my_player_1_card_value = get_card_value(my_card)
            my_total_player_1_card_value = my_total_player_1_card_value + my_player_1_card_value      
            print("Players 1 total card value is {}".format(my_total_player_1_card_value))
            
        elif my_player_1_choice_lower == 's':
            print("Player 1 decided to stay.")
            my_player_1_turn = False
            
        else:
            print("Bad value entered!")

        print("Player 1 selected {}:\n ".format(my_player_1_choice_lower))
            
        if my_total_player_1_card_value > blackjack:
            print("Player 1's hand is {} which is greater than {}. Player 1 is busted.".format(my_total_player_1_card_value,blackjack))
            my_player_1_turn = False
            my_player_2_turn = False
            player_2_wins+=1

    # Get value of each card delt for player 1
    while my_player_2_turn:

        print ("Player 2's cards:")
        my_total_player_2_card_value = 0
        for player_2_card in player_2_list:
            my_player_2_card_value = get_card_value(player_2_card)
            my_total_player_2_card_value = my_total_player_2_card_value + my_player_2_card_value
            print(player_2_card,end=" ")

        print("\n")
        print("Players 2 total card value is {}".format(my_total_player_2_card_value))
        print_lines()

        player_2_card_flag = True
        while player_2_card_flag: 
            if my_total_player_2_card_value < my_total_player_1_card_value:
                my_deck,my_card = get_card(my_deck)
                print("Card received: {}".format(my_card))
                player_2_list.append(my_card)
                my_player_2_card_value = get_card_value(my_card)
                my_total_player_2_card_value = my_total_player_2_card_value + my_player_2_card_value

            elif my_total_player_2_card_value > my_total_player_1_card_value:
                my_player_2_turn = False
                player_2_card_flag = False
                
            elif my_total_player_2_card_value == my_total_player_1_card_value:
                my_player_2_turn = False
                player_2_card_flag = False
             
        if my_total_player_2_card_value > blackjack:
            print("Player 2's hand is {} which is greater than {}. Player 2 is busted.".format(my_total_player_2_card_value,blackjack))
            print("Player 1 wins with a hand totaling {}".format(my_total_player_1_card_value))
            my_player_2_turn = False
            player_1_wins+=1
        
    # Check who wins if no bust.
    if my_total_player_1_card_value <= blackjack:
        if my_total_player_2_card_value <= blackjack:
            if my_total_player_1_card_value > my_total_player_2_card_value:
                print("Player 1 wins with a hand totaling {}".format(my_total_player_1_card_value))
                player_1_wins+=1
            elif my_total_player_1_card_value < my_total_player_2_card_value:
                if my_total_player_1_card_value < blackjack:
                    print("Player 2 wins with a hand totaling {}".format(my_total_player_2_card_value))
                player_2_wins+=1
            elif my_total_player_1_card_value == my_total_player_2_card_value:
                print("Player 1 and Player 2 both had {}. It is a push.".format(my_total_player_1_card_value))
                players_push+=1
    print("\n")

    number_of_hands+=1
    #print("Number of cards left is {}".format(len(my_deck)))

    print_lines()

    my_continue_game_choice=input("Play again (y/n)?")
    if my_continue_game_choice.lower() != "y":
        continue_game = False
        
# Display totals
print_lines()
print("Total number of games played: {}.".format(number_of_hands))
print("Player 1 wins: {}".format(player_1_wins))
print("Player 2 wins: {}".format(player_2_wins))
print("Player Pushes: {}".format(players_push))
