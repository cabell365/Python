# Dice Game
# You throw up to 5 dice 3 times
# Each lucky number rolled removes the number of die available to roll
#
# Here is the scoring for the game
# 5 of your lucky number: 25 points
# 4 of your lucky number: 20 points
# 3 of your lucky number: 15 points
# 2 of your lucky number: 10 points
# 1 of your lucky number: 5 points

from random import randint

print("You score points for every time you roll your lucky number.")
print("A die is removed each time your lucky number is rolled.")
print("Here is the scoring for the game")
print("* 5 of your lucky number: 25 points")
print("* 4 of your lucky number: 20 points")
print("* 3 of your lucky number: 15 points")
print("* 2 of your lucky number: 10 points")
print("* 1 of your lucky number: 5 points")
print("\n")

my_dice_values = [1,2,3,4,5,6]
my_points_dict = {0:0,1:5,2:10,3:15,4:20,5:25}
my_points_message_dict = {0:"You have no luck at all.",
                  1:"You have a tiny bit of luck.",
                  2:"You luck level is rising. ",
                  3:"You could be on a roll!",
                  4:"You are a very lucky person!",
                  5:"You should play the lottery!"}
my_roll_list = []

my_winning_num_str = ""
my_winning_num = 0
my_max_die = 5
my_max_roles = 3
my_roll_cnt = 0
my_min_die_val = 1
my_max_die_val = 6
my_winning_num_cnt = 0
is_not_valid_num = True

while is_not_valid_num:
    my_winning_num_str=input("Please enter your lucky number between {} and {}: ".format(my_min_die_val,my_max_die_val))
    if my_winning_num_str.isdecimal():
        my_winning_num = int(my_winning_num_str)
        if my_winning_num in my_dice_values:
            is_not_valid_num = False
        else:
            print("The number selected {} is not between {} and {}:".format(my_winning_num,my_min_die_val,my_max_die_val))
            is_not_valid_num = True
    elif len(my_winning_num_str) > 1:
        print("The value entered is greater than 1 value!")
        is_not_valid_num = True
    else:
        print("You entered non-decimal characters!")
        is_not_valid_num = True
    
while my_roll_cnt != my_max_roles:
 
    print("\n")
    my_roll_cnt+=1
    print("Roll number {}:".format(my_roll_cnt))
    for i in range(my_max_die - my_winning_num_cnt):
        my_roll_list.append(randint(my_min_die_val,my_max_die_val))
        
    print(my_roll_list)
    for my_die in my_roll_list:
        if my_die == my_winning_num:
            my_winning_num_cnt+=1

    my_roll_list.clear()

print("\nYour {} roles produced {} {}'s".format(my_max_roles,my_winning_num_cnt,my_winning_num))
print("Congratulations. You scored {} points!".format(my_points_dict[my_winning_num_cnt]))
print("{}".format(my_points_message_dict[my_winning_num_cnt]))

