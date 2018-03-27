from unittest import TestCase
from unittest.mock import Mock

# Think -> Red -> Green -> Refactor
#
# Guideline 1: Always start with outputs
# 
# Guideline 2: Behavior slicing
#
# Guideline 3: Simplify
# Start with 2 friends
#

# Two friends: Alice & Bob
#               split 50-50
#   Inputs                  Outputs
#   Bob payed 40€          Alice owes Bob 20€
#             split by consumption
#   Bob payed 30             Alice owes Bob 20€
#   Bob payed 50             Alice owes Bob 20€
#


def compute_balance_fifty_fifty(expenses_made, friends):
    expense = expenses_made
    number_of_friends = len(friends)
    debt = expense / number_of_friends
    production_code = debt
    return production_code

class TestGoodFriends(TestCase):


    def setUp(self):
        pass

    # TODO: Introduce the concept of money later
    def test_Bob_payed_40_euro_split_fifty_fifty_Alice_owes_20_euro_to_Bob(self):
        # Arrange
        expected = 20
        expenses_made = 40
        friends = ["Bob", "Alice"]

        # Act
        actual = compute_balance_fifty_fifty(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_100_split_fifty_fifty_Alice_owes_50_euro_toBob(self):
        # Arrange
        expected = 50
        expenses_made = 100
        friends = ["Bob", "Alice"]

        # Act
        actual = compute_balance_fifty_fifty(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_120_split_fifty_fifty_AliceAndJohn_owe_40_each_toBob(self):
        # Arrange
        expected = 40
        expenses_made = 120;
        friends = ["Bob", "Alice", "John"]

        # Act
        actual = compute_balance_fifty_fifty(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)