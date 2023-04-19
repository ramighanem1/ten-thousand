"""
- Handle rolling dice
- Add `roll_dice` static method to GameLogic class.
- The input to `roll_dice` is an integer between 1 and 6.
- The output of `roll_dice` is a tuple with random values between 1 and 6.
- The length of tuple must match the argument given to `roll_dice` method.
"""
import pytest
from ten_thousand.game_logic import GameLogic

# pytestmark = [pytest.mark.version_1]

@pytest.mark.parametrize("num_dice,expected_length",
                         [
                            (1,1),
                            (2,2),
                            (3,3),
                            (4,4),
                            (5,5),
                            (6,6),
                         ],
)
def test_all_dice_rolls(num_dice,expected_length):
    values = GameLogic.roll_dice(num_dice)
    assert len(values) == expected_length
    for value in values:
        assert 1 <= value <= 6