
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

    # Start the round
    while True:
        # Roll the dice
        roll = ROLLER_FUNC(remaining_dices)

        # Display the dice roll
        print(f"Rolling {remaining_dices} dice...")
        print("*** {} ***".format(" ".join(str(i) for i in roll)))

        # Prompt the user to select which dice to keep
        user_input = input("Enter dice to keep, or (q)uit:\n> ")
        if user_input == 'q':
            return -1
        
        keep_dice = tuple(int(i) for i in user_input)

        #check if keep_dice in roll

        # Keep the selected dice and calculate the score
        roll = tuple(die for die in roll if die in keep_dice)

        # add score to round score
        round_score += GameLogic.calculate_score(roll)

        remaining_dices -= len(roll)

        # Display the round score 
        print(f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
        
        # prompt the user to roll again, bank points or quit
        if remaining_dices == 0:
            print("(b)ank your points or (q)uit:")
        else:
            print("(r)oll again, (b)ank your points or (q)uit:")

        # Get user input and validate it
        user_input = input("> ")
        if user_input == "q":
            # Quit the game
            return -1
        elif user_input == "b":
            # Bank points
            return round_score
    

def start_game():
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

    end_game_message(total_score)

    
    
def play(roller=GameLogic.roll_dice):
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
        start_game()
    else:
        decline_game_message()


if __name__ == '__main__':
    play()