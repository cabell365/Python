#
# Basic Craps game
#
# The first dice roll will set the come point. You win if it is a natural (7, 11)
# and lose if it is craps (2, 3, 12). Other rolls will make you a winner if the come point is repeated before a 7 is rolled.
#
from random import randint
import sys

def roll_die():
    
    my_role_list = []
    my_min_die_val = 1
    my_max_die_val = 6
    my_dice_values = [1,2,3,4,5,6]

    my_die_roll_1=randint(my_min_die_val,my_max_die_val)
    my_die_roll_2=randint(my_min_die_val,my_max_die_val)
    
    my_role_list.append(my_die_roll_1)
    my_role_list.append(my_die_roll_2)
    
    return my_role_list

def craps_win(total_die):
    
    craps_win_list = [7,11]
    
    if total_die in craps_win_list:
        is_crap_win=True
    else:
        is_crap_win=False
    
    return is_crap_win
    
def crapped_out(total_die):
    
    crapped_out_list = [2,3,12]
    
    if total_die in crapped_out_list:
        is_crapped_out=True
    else:
        is_crapped_out=False
    
    return is_crapped_out   

def print_lines():
    number_of_lines = 100
    print(number_of_lines * "-")
    print("\n")

def main():

    is_first_role = True
    is_still_rolling_die = True
    my_original_roll = []
    my_new_roll= []
    my_total_original_role=0
    my_total_new_roll=0
    
    print_lines()
    print("First roll of the dice:")
 
    while is_still_rolling_die:
        if is_first_role:
            my_original_roll=roll_die()
            my_total_original_role = my_original_roll[0] + my_original_roll[1]
            print("Die 1: {}".format(my_original_roll[0]))
            print("Die 2: {}".format(my_original_roll[1]))
            print("Total Die Value: {}\n".format(my_total_original_role))

            # Check if won on first role
            is_crap_win=craps_win(my_total_original_role)
            if is_crap_win:
                print("You win on first roll!")
                is_still_rolling_die = False
            else:
                # Check if crapped out in first roll
                is_crapped_out=crapped_out(my_total_original_role)
                if is_crapped_out:
                    print("You crapped out!")
                    is_still_rolling_die = False
                    
            is_first_role = False
        else:
            # roll again
            my_new_roll=roll_die()
            my_total_new_roll = my_new_roll[0] + my_new_roll[1]
            print("Next role")
            print("Die 1: {}".format(my_original_roll[0]))
            print("Die 2: {}".format(my_original_roll[1]))
            print("Roll Total: {}\n".format(my_total_new_roll))
        
        if my_total_original_role == my_total_new_roll:
            print("You win!")
            is_still_rolling_die = False
        elif my_total_new_roll == 7:
            print("You lose because you rolled 7 before getting {}.".format(my_total_original_role))
            is_still_rolling_die = False
                       
if __name__ == "__main__":
    # execute only if run as a script
    main()

sys.exit
    
    

