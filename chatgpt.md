# First use 

## we tried to use it to calculate the score the result is not good so we build it from scratch

## prompt : 
```
i have dictionary with key and value i need to get count where value =2
``` 

## output code

```
my_dict = {"a": 1, "b": 2, "c": 2, "d": 3, "e": 4, "f": 4}

count = 0
for value in my_dict.values():
    if value == 2:
        count += 1
print("Number of values that occur exactly twice in the dictionary:", count)

```

# second use 

## prompt : 
```
1) i have function1 that call function2 inside while how to break while function1 from function2 
2) another way
3) another way
4) function2 return number
```
## output code : 

```
def function1():
    while True:
        # do something
        result = function2()
        if result == 42:
            break
def function2():
    if some_condition:
        return 42
    else:
        return 0
```


# third use 
## prompt : 
```
compleat start_round function

this is command line :

Starting round 1
Rolling 6 dice...
*** 3 2 5 4 3 3 ***
Enter dice to keep, or (q)uit:
> 3335
You have 350 unbanked points and 2 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b

this is the code :
"def start_round(round_number):
    """
    return round score or -1 if user chose to quit
    """
    start_round_message(round_number)
    remaining_dices = 6
    round_score = 0

    # start round
    while True:
        roll = ()
        round_score+=GameLogic.calculate_score(roll)

        print(f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
        print(f"(r)oll again, (b)ank your points or (q)uit:")

        # get user input
        user_input = input("> ")


        if user_input == "q":
            # quit game
            return -1
        elif user_input == "b":
            # bank points
            return round_score"
```
## output code : 

```
def start_round(round_number):
    """
    Return round score or -1 if user chose to quit
    """
    start_round_message(round_number)
    remaining_dices = 6
    round_score = 0

    # start round
    while True:
        roll = tuple(random.randint(1, 6) for _ in range(remaining_dices))
        print("Rolling {} dice...".format(remaining_dices))
        print("*** {} ***".format(" ".join(str(i) for i in roll)))

        # get user input
        while True:
            user_input = input("Enter dice to keep, or (q)uit:\n> ")
            if user_input == 'q':
                return -1
            try:
                keep_dice = tuple(int(i) for i in user_input)
                if len(keep_dice) <= remaining_dices:
                    break
                else:
                    print("You must keep at most {} dice".format(remaining_dices))
            except ValueError:
                print("Invalid input")

        roll = tuple(die for die in roll if die in keep_dice)
        remaining_dices -= len(roll)
        round_score += GameLogic.calculate_score(roll)

        print(f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
        if remaining_dices == 0:
            print("(b)ank your points or (q)uit:")
        else:
            print("(r)oll again, (b)ank your points or (q)uit:")

        # get user input
        while True:
            user_input = input("> ")
            if user_input == "q":
                # quit game
                return -1
            elif user_input == "b":
                # bank points
                return round_score
            elif user_input == "r":
                # roll again
                break
            else:
                print("Invalid input")

```