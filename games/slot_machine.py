# Slot machine game.
# You are granted 100 credits to start
# Play the slots, earn credits!
# There are winning combinations that earn big credits!
# You get 5 credits if you get duplicate values and no lemons
#
from random import randint

def get_slot_symbols():
    slot_symbols=[
        "BAR",
        "LEMON",
        "CHERRY",
        "GRAPES",
        "BELL",
        "777",
        "ORANGE"
        ]

    return slot_symbols

def get_slot_wheel(slot_symbols_list):
    
    slot_wheel_list = []
    
    slot_symbols_index_1=randint(0,len(slot_symbols_list)-1)
    slot_wheel_list.append(slot_symbols_list[slot_symbols_index_1])
        
    slot_symbols_index_2=randint(0,len(slot_symbols_list)-1)
    slot_wheel_list.append(slot_symbols_list[slot_symbols_index_2])
        
    slot_symbols_index_3=randint(0,len(slot_symbols_list)-1)
    slot_wheel_list.append(slot_symbols_list[slot_symbols_index_3])
        
    return slot_wheel_list

def get_combo_winnings(slot_symbols):
    
    winnings = 0
    slot_winning_combo_list = []
    slot_winning_combos = {
        
        5000: "777,777,777",
        4000 : "BAR,BAR,BAR",
        3000 : "GRAPES,GRAPES,GRAPES",
        2000 : "CHERRY,CHERRY,CHERRY",
        1000 : "ORANGE,ORANGE,ORANGE",
        500 : "BELL,BELL,BELL",
        400: "777,777,,BAR",
        300: "777,BAR,,BAR",
        200: "777,GRAPES,GRAPES",
        100: "777,CHERRY,CHERRY",
        80: "BAR,CHERRY,BAR",
        70: "CHERRY,BAR,CHERRY",
        60: "GRAPES,CHERRY,CHERRY",
        50: "CHERRY,BELL,BAR",
        40: "BELL,CHERRY,GRAPE",
        30: "BELL,CHERRY,ORANGE",
        20: "BELL,GRAPE,ORANGE",
        10: "ORANGE,GRAPE,CHERRY"       
        
        }

    # Check for winning combinations by comparing lists
    for credits, slot_winning_combo in slot_winning_combos.items():
        slot_winning_combo_list=slot_winning_combo.split(",")
        if slot_winning_combo_list == slot_symbols:
            winnings = credits
    
    return winnings 

def get_duplicate_winnings(slot_symbols):

    winnings = 0
    
    # Check for duplicates. Get 2 of a kind, get 5 credits
    for slot_symbol in slot_symbols:
        if len(slot_symbols) == len(set(slot_symbols)):
            winnings = 0
        else:
            winnings = 5

    # If any value is a Lemon then no winnings
    for slot_symbol in slot_symbols:
        if slot_symbol == "LEMON":
            winnings = 0

    return winnings 

def main():

    my_winnings = 0
    my_credits = 100
    my_play_amount = 5
    continue_playing = True
    
    # Get list of slot symbols
    my_slot_symbols_list=get_slot_symbols()
    
    while continue_playing:
        
        my_slot_wheel_list = []
        
        my_slot_wheel_list=get_slot_wheel(my_slot_symbols_list)
        
        my_credits=my_credits-my_play_amount
        my_winnings=get_combo_winnings(my_slot_wheel_list)
        if my_winnings == 0:
            my_winnings=get_duplicate_winnings(my_slot_wheel_list)
        my_credits=my_credits+my_winnings
        
        print("Here are the results of playing the one arm bandit!")
        print (my_slot_wheel_list)
        if my_winnings == 0:
            print("\nNo $ won this time. Better luck on your next spin!")
        else:
            print("\nYou won {} credits!\n".format(my_winnings))
            
        print("Your current credit is {}\n".format(my_credits))
        
        if my_credits == 0:
            print("Sorry, you lost all of your money!")
            continue_playing = False
            
        my_end_selection=input('Do you want to (q)uit? Press any key to continue playing the slots: ')
        if my_end_selection.lower() == 'q':
            continue_playing=False
            print("You earned {} credits!".format(my_credits))
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
    
        
    