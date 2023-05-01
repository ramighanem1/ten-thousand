import random
from collections import Counter

class GameLogic:

    def __str__(self):
        return f"GameLogic Class"

    def __repr__(self):
        return f"GameLogic Class"
    
    @staticmethod
    def calculate_score(dice):
        """
        Calculate the score for a given roll of dice.

        Args:
        dice: tuple of integers that represent a dice roll
        """
        count = Counter(dice)
        deletedKey=[]
        score = 0
        Pairscount = 0
        ThreeOfKindcount=0

        # check Straight 1- 6
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            return 1500
                
        # count Pairs and Three of a kind
        for value, num_dice in count.items():
            if num_dice == 2:
                Pairscount += 1
                deletedKey.append(value)
            elif num_dice == 3:
                ThreeOfKindcount+=1
                deletedKey.append(value)

        # check Three Pairs          
        if Pairscount==3:
            score+=1500
            for key in deletedKey:
                del count[key]
        # check Full House
        elif Pairscount==1 and ThreeOfKindcount==1:
            score+=1500
            for key in deletedKey:
                del count[key]

        
        for value, num_dice in count.items():
            # check 6 of a kind
            if num_dice == 6:
                if value == 1:
                    return 8000
                elif value == 2:
                    return 1600
                elif value == 3:
                    return 2400
                elif value == 4:
                    return 3200
                elif value == 5:
                    return 4000
                elif value == 6:
                    return 4800
            # check 5 of a kind
            elif num_dice == 5:
                if value == 1:
                    score += 4000
                else:
                    score += value * 400
                num_dice-=5
            # check 4 of a kind
            elif num_dice == 4:
                if value == 1:
                    score += 2000
                else:
                    score += value * 200
                num_dice-=4
            # check 3 of a kind
            elif num_dice==3:
                if value == 1:
                    score += 1000
                else:
                    score += value * 100
                num_dice -= 3
            # check Single 1 and Single 5
            else:
                if value == 5:
                    score += num_dice * 50
                elif value == 1:
                    score += num_dice * 100
                
        return score

    @staticmethod
    def roll_dice(dice_count):
        """
        returns a list of the values of the rolled dice 

        Args:
        dice_count: integer between 1 and 6 as number of dice to be rolled
        """
        dice = []
        for _ in range(dice_count):
            die = random.randint(1, 6)
            dice.append(die)
        return tuple(dice)
    

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        Check if a given set of dice can be kept from a roll
        """
        roll_counter = Counter(roll)
        keeper_counter = Counter(keepers)
        # Check if keepers is a subset of roll
        if keeper_counter - roll_counter != Counter():
            return False
        # Check if any dice were kept more times than they appear in the roll
        for die, count in keeper_counter.items():
            if count > roll_counter[die]:
                return False
        return True
    
    @staticmethod
    def get_scorers(test_input):
        """
        Returns a tuple of letters that are considered "scorers" in the input word, meaning they can be removed to form
        words with different scores.
        """
        main_score = GameLogic.calculate_score(test_input)
        scorers = [val for i, val in enumerate(test_input) if GameLogic.calculate_score(test_input[:i] + test_input[i+1:]) != main_score]
        return tuple(scorers)