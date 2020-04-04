def print_grid_coord():
    print("The x coordinate or the y coordinate only allows the numbers: 0,1,2")
    print("List of coordinates for the grid:")
    
    tic_tac_toe_grid_coord = [
    ["0,0", "0,1", "0,2"],
    ["1,0", "1,1", "1,2"],
    ["2,0", "2,1", "2,2"]]
    
    for x in tic_tac_toe_grid_coord:
        print("{}".format(x))
    print("\n")
    
def print_grid(tic_tac_toe_grid):
    print("\n")
    for x in tic_tac_toe_grid:
        print("{}".format(x))
    print("\n")

def coord_chosen(x_coord, y_coord, tic_tac_toe_grid):
    x_y_coord = tic_tac_toe_grid[x_coord][y_coord]
    return x_y_coord

def valid_coord(coord):
    my_valid_coord = [0,1,2]
    if len(str(coord)) > 1:
        return False
    elif coord in my_valid_coord:
        return True
    else:
        return False
    
def check_across(x_coord,tic_tac_toe_grid):
    cnt=0
    x_list = []
    x_list = tic_tac_toe_grid[x_coord]
    for x in range(len(x_list)):
        cnt = cnt + ord(x_list[x])
    return cnt

def check_down(y_coord,tic_tac_toe_grid):
    cnt=0
    for x in range(len(tic_tac_toe_grid)):
        cnt = cnt + ord(tic_tac_toe_grid[x][y_coord])
    return cnt
 
def check_diagonal_down(tic_tac_toe_grid):
    cnt=0
    for j in range(len(tic_tac_toe_grid)):
        cnt = cnt + ord(tic_tac_toe_grid[j][j])
    return cnt

def check_diagonal_up(tic_tac_toe_grid):
    cnt=0
    for k in range(len(tic_tac_toe_grid)):
        x_index = (len(tic_tac_toe_grid)-1) - k
        cnt = cnt + ord(tic_tac_toe_grid[x_index][k])
    return cnt

def check_winner(tic_tac_toe_grid):
    X_O_win_dict = {264:"X", 237:"O"}
    x_cnt = 0
    y_cnt = 0
    diag_up_cnt = 0
    diag_down_cnt = 0
    win_value = None
    
    for x in range(len(tic_tac_toe_grid)):
        x_cnt = check_down(x,tic_tac_toe_grid)
        if x_cnt in X_O_win_dict:
            win_value = X_O_win_dict[x_cnt]      
    
    for y in range(len(tic_tac_toe_grid)):    
        y_cnt = check_across(y,tic_tac_toe_grid)
        if y_cnt in X_O_win_dict:
            win_value = X_O_win_dict[y_cnt]
    
    diag_up_cnt = check_diagonal_up(tic_tac_toe_grid)
    if diag_up_cnt in X_O_win_dict:
        win_value = X_O_win_dict[diag_up_cnt]

    diag_down_cnt = check_diagonal_down(tic_tac_toe_grid)
    if diag_down_cnt in X_O_win_dict:
        win_value = X_O_win_dict[diag_down_cnt]
        
    return win_value

def print_rules():
    print("\n------------------------------------------------------------------------------")
    print("The script is a simple 'tic tac toe' game.")
    print("The game uses x,y coordinates to select an X or O")
    print("Open coordinates are displayed with an asterix '*'")
    print("X is always first and O is always second")
    print("You can exit at anytime by terminating the program with Ctrl C")
    print("Lets play tic tac toe!")
    print("-------------------------------------------------------------------------------\n")

# print rules and grid values
print_rules()
print_grid_coord()

# Start of the main program
def main():   

    # Define tic tac toe grid
    my_tic_tac_toe_grid = [
        ["*", "*", "*"],
        ["*", "*", "*"],
        ["*", "*", "*"]]
    
    # Default variables
    is_game_over = False
    cnt_selections = 0
    max_selections = 9
    my_x_coord = 0
    my_y_coord = 0
    my_win_value = None
    
    while not is_game_over:

        # Default variables
        my_x_y_coord = ""
        is_valid_x_value = False
        is_valid_y_value = False

        # Determine which player's turn it is
        if cnt_selections % 2 == 0:
            print("Player 1's turn:")
        else:
            print("Player 2's turn:")

        # Stay in a loop until a open coordinate is given
        while my_x_y_coord != "*":        

            # Validate x coordinate
            while not is_valid_x_value:
                my_x_coord_str=input("Please select x coordinate: ")
                if my_x_coord_str.isdecimal():
                    my_x_coord = int(my_x_coord_str)
                    is_valid_x_value = valid_coord(my_x_coord)
                    if not is_valid_x_value:
                        print("X coordinate must be 0,1 or 2!")
                        is_valid_x_value = False
                    else:
                        is_valid_x_value = True
                else:
                    print("X coordinate must be 0,1 or 2!")

            # Validate y coordinate
            while not is_valid_y_value:              
                my_y_coord_str=input("Please select y coordinate: ")
                if my_y_coord_str.isdecimal():
                    my_y_coord = int(my_y_coord_str)
                    is_valid_y_value = valid_coord(my_y_coord)
                    if not is_valid_y_value:
                        print("Y coordinate must be 0,1 or 2!")
                        is_valid_y_value = False
                    else:
                        is_valid_y_value = True
                else:
                    print("Y coordinate must be 0,1 or 2!")
 
            # Check that the coordinate must be an asterix
            my_x_y_coord = coord_chosen(my_x_coord,my_y_coord,my_tic_tac_toe_grid)
            if my_x_y_coord != "*":
                print ("Selection is already chosen with an {}. Chose different coordinates".format(my_x_y_coord))
                is_valid_x_value = False
                is_valid_y_value = False

        #Game starts with X, Even = X, Odd = O
        if cnt_selections % 2 == 0:
            my_tic_tac_toe_grid[my_x_coord][my_y_coord] = "X"
        else:
            my_tic_tac_toe_grid[my_x_coord][my_y_coord] = "O"

        # Increment the number of selections
        #cnt_selections += 1

        # Print current grid
        print_grid(my_tic_tac_toe_grid)

        # Increment the number of selections
        cnt_selections += 1
        
        # Verify if a winner is found
        my_win_value = check_winner(my_tic_tac_toe_grid)
        if my_win_value is not None:
            print("The winner is {}!".format(my_win_value))
            is_game_over = True
            
        # Set flag to exit if maximum number of choices is made
        if max_selections == cnt_selections and my_win_value is None:
            print("Scratch game. No winner!")
            is_game_over = True
                 
# Execute main program
if __name__== "__main__":
    main()
        
