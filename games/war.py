# Very simple game of War
# Two computerized players.
# Each player selects the first card on the deck
# Here are the rules:
# * The highest card wins
# * Aces are highest, 2 is lowest
# * Player with highest card receives the card from the other player.
#      and both cards are moved to the back of the deck
# * Game Winner is determined by who has the most cards after X hands are played
# * Game is simplified. Both players cards are moved to the back of the deck in a tie

from random import randint

def build_deck():
    deck_list = []

    suit_list = ["S","H","D","C"]
    face_card_list = ["A","K","Q","J"]
    numbered_card_list = ["2","3","4","5","6","7","8","9","10"]

    for suit in suit_list:
        for face_card in face_card_list:
            face_card_suit = face_card + "-" + suit
            deck_list.append(face_card_suit)

    for suit in suit_list:
        for numbered_card in numbered_card_list:
            numbered_card_suit = numbered_card + "-" + suit
            deck_list.append(numbered_card_suit)
            
    return deck_list

def deal_cards(deck_list):
    
    init_card_delt_cnt = 0
    max_deck_len = 51
    player_1_list = []
    player_2_list = []
       
    while init_card_delt_cnt != max_deck_len:
        deck_list,card = get_card(deck_list)
        #print(card)

        if init_card_delt_cnt % 2 == 0:
            player_1_list.append(card)
        else:
            player_2_list.append(card)
           
        init_card_delt_cnt+=1
        
    # Code added here to add last card to player 2's list
    # Will fix eventually because there should be a better way
    player_2_list = player_2_list + deck_list
      
    return player_1_list, player_2_list

def get_card(deck):  
    is_not_card_available = True
    while is_not_card_available:
        card_delt = randint (0,len(deck)-1)
        if card_delt < len(deck)-1:
            if deck[card_delt] in deck:
                card_found=deck[card_delt]
                deck.remove(deck[card_delt])
                is_not_card_available = False
    return deck, card_found

def get_card_value(card):
    card_value_dict = {"A":14,"K":13,"Q":12,"J":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
    return card_value_dict[card.split("-",1)[0]]

def play_cards(player_1_list, player_2_list):

    transaction_list=[]
    player_1_card=player_1_list[0]
    player_2_card=player_2_list[0]
    
    player_1_card_value=get_card_value(player_1_card)
    transaction_list.append(player_1_card)
    
    player_2_card_value=get_card_value(player_2_card)
    transaction_list.append(player_2_card)

    # test_list.append(test_list.pop(test_list.index(5))) 
    if player_1_card_value > player_2_card_value:
        player_1_list.append(player_2_card)
        player_2_list.remove(player_2_card)
        player_1_list.append(player_1_list.pop(player_1_list.index(player_1_card)))
        
        transaction_list.append("1")
    elif player_1_card_value < player_2_card_value:
        player_2_list.append(player_1_card)
        player_1_list.remove(player_1_card)
        player_2_list.append(player_2_list.pop(player_2_list.index(player_2_card)))
        transaction_list.append("2")
    else:
        player_1_list.append(player_1_list.pop(player_1_list.index(player_1_card)))
        player_2_list.append(player_2_list.pop(player_2_list.index(player_2_card)))
        transaction_list.append("3")
        
    return player_1_list, player_2_list, transaction_list             

def print_lines():
    number_of_lines = 100
    print(number_of_lines * "-")
    print("\n")

def print_rules():
    print("This is a game of card based War.")
    print("Player two is the computer")
    print("Here are the basic rules of the game:")
    print("\tTwo computer players play the card game War")
    print("\tEach player is delt 26 cards")
    print("\tEach player plays a card and highest card wins")
    print("\tThe winner takes the loser's card and places both cards at the back of the deck")
    print("\tThe cards of the deck are represented as the following:")
    print("\tThe deck suits are 'S' for Spades, 'H' for Hearts, 'D' for Diamonds and 'C' for Clubs")
    print("\tThe 'A' is Ace, 'K' is King, 'Q' is Queen and 'J' is Jack")
    print("\tThe non-face cards are represented with the numbers 2 through 10")

# Build the initial deck
my_deck_list = build_deck()

max_number_of_hands = 20
number_of_hands = 0
my_player_1_list = []
my_player_2_list = []
my_transaction_list = []

# Deal Cards
my_player_1_list, my_player_2_list=deal_cards(my_deck_list)

# print rules
print_lines()
print_rules()

# Play a hand
while max_number_of_hands != number_of_hands:
    
    my_player_1_list, my_player_2_list,my_transaction_list=play_cards(my_player_1_list, my_player_2_list)
    print("Player One's card: {}".format(my_transaction_list[0]))
    print("Player Twos's card: {}".format(my_transaction_list[1]))
    print()

    print("Player one length:",len(my_player_1_list))
#     for my_player1_card in my_player_1_list:
#         print(my_player1_card)

    print("Player two length:",len(my_player_2_list))
#     for my_player2_card in my_player_2_list:
#         print(my_player2_card)
    print()
    
    number_of_hands+=1
