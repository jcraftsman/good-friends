from unittest import TestCase


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
#   Bob payed 100€


def compute_balance_fifty_fifty(expenses_made, friends):
    expense = expenses_made
    number_of_friends = len(friends)
    debt = expense / number_of_friends
    return debt


def get_debtor_list(friends, payer):
    def comparator(x): return -1 if x == payer else 1

    friends_sorted_with_payer_first = sorted(friends, key=comparator)
    debtors = friends_sorted_with_payer_first[1:]
    return debtors


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
        expenses_made = 120
        friends = ["Bob", "Alice", "John"]

        # Act
        actual = compute_balance_fifty_fifty(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_is_debitor_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice"]
        expected = ["Alice"]

        # Act
        actual = get_debtor_list(friends, payer)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_and_John_are_debtors_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice", "John"]
        expected = ["Alice", "John"]

        # Act
        actual = get_debtor_list(friends, payer)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_John_and_Claire_are_debtors_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice", "John", "Claire"]
        expected = ["Alice", "John", "Claire"]

        # Act
        actual = get_debtor_list(friends, payer)

        # Assert
        self.assertEquals(expected, actual)
