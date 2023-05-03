from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic

ROLLER_FUNC = GameLogic.roll_dice

def welcome_game_message():
    """
    Display Welcome Message
    """
    print("Welcome to Ten Thousand")

def decline_game_message():
    """
    Display decline Game Message
    """
    print("OK. Maybe another time")

def end_game_message(total_score):
    """
    Display end Game Message
    """
    print(f"Thanks for playing. You earned {total_score} points")

def start_round_message(round_number):
    """
    Display start round Message
    """
    print(f"Starting round {round_number}")


def start_round(round_number):
    """
    return round score or -1 if user chose to quit
    """
   # Display the start round message
    start_round_message(round_number)

    # Initialize the number of remaining dice and round score
    remaining_dices = 6
    round_score = 0
    num_of_roll = 0

    # Start the round
    while True:
        # Roll the dice
        roll = ROLLER_FUNC(remaining_dices)
        #increas roll count by 1
        num_of_roll+=1

        # Display the dice roll
        print(f"Rolling {remaining_dices} dice...")

        while True:
            # Handel Zilch
            print("*** {} ***".format(" ".join(str(i) for i in roll)))
            if GameLogic.calculate_score(roll) ==0:
                print('****************************************')
                print('**        Zilch!!! Round over         **')
                print('****************************************')
                return 0
            # Prompt the user to select which dice to keep
            print("Enter dice to keep, or (q)uit:")
            user_input = input('> ')
            if user_input == 'q':
                return -1
            
            keep_dice = tuple(int(i) for i in user_input if i !=' ')

            #check if keep_dice in roll
            if(GameLogic.validate_keepers(roll,keep_dice)):
                break
            else:
                print('Cheater!!! Or possibly made a typo...')

        # Keep the selected dice and calculate the score
        roll = tuple(die for die in roll if die in keep_dice)

        # add score to round score
        round_score += GameLogic.calculate_score(roll)

        remaining_dices -= len(roll)


        # Display the round score
        if (round_score == 1500):
            if remaining_dices==1:
                print(f"You have {round_score} unbanked points and 5 dice remaining")
            else:
                print(f"You have {round_score} unbanked points and 6 dice remaining")

        else:
            print(f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
        
        # prompt the user to roll again, bank points or quit
        if remaining_dices == 0 and num_of_roll !=1:
            print("(b)ank your points or (q)uit:")
        elif remaining_dices>0:
            print("(r)oll again, (b)ank your points or (q)uit:") 
        elif remaining_dices == 0 and num_of_roll ==1:
            print("(r)oll again, (b)ank your points or (q)uit:")
            remaining_dices+=6
            num_of_roll=0

        # Get user input and validate it
        user_input = input("> ")
        if user_input == "q":
            # Quit the game
            return -1
        elif user_input == "b":
            # Bank points
            return round_score
    

def start_game(num_rounds):
    """
    start the game
    """
    round_number = 1
    total_score = 0

    while True:
        # start round
        round_score = start_round(round_number)

        # stop game if user input q
        if round_score == -1:
            break

        #round banked message
        print(f"You banked {round_score} points in round {round_number}")

        # add banked to Total Score
        total_score+=round_score

        # printTotal Score
        print(f"Total score is {total_score} points")

        # incras round number
        round_number+=1

        if(round_number>num_rounds):
            break

    end_game_message(total_score)

    
    
def play(roller=GameLogic.roll_dice,num_rounds=20):
    """
    start Ten Thousand game
    Args:
    roller : rolled dice values (optional)
    """
    # save roller in global to keep track the rollers
    global ROLLER_FUNC
    ROLLER_FUNC = roller

    #print welcome message
    welcome_game_message()

    # prompt the user to start the game or decline
    print("(y)es to play or (n)o to decline")

    #get user input
    user_input = input("> ")

    #handel user input
    if user_input == "y":
        start_game(num_rounds)
    else:
        decline_game_message()


if __name__ == '__main__':
    play(num_rounds=1)