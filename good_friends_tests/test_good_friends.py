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
#
#   Bob payed 120€,
#   Bob payed 30€          Alice owes Bob 75€
#
#             split by consumption
#   Bob payed 30             Alice owes Bob 20€
#   Bob payed 50             Alice owes Bob 20€
#
#   Bob payed 100€


def compute_uniform_debt(expenses_made, friends):
    expense = expenses_made
    number_of_friends = len(friends)
    debt = expense / number_of_friends
    return debt


def get_debtors(friends, payer):
    return set(friends) - {payer}


class TestGoodFriends(TestCase):

    # TODO: Introduce the concept of money later

    def setUp(self):
        pass

    def test_Bob_payed_40_euro_split_fifty_fifty_Alice_owes_20_euro_to_Bob(self):
        # Arrange
        expected = 20
        expenses_made = 40
        friends = ["Bob", "Alice"]

        # Act
        actual = compute_uniform_debt(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_100_split_fifty_fifty_Alice_owes_50_euro_toBob(self):
        # Arrange
        expected = 50
        expenses_made = 100
        friends = ["Bob", "Alice"]

        # Act
        actual = compute_uniform_debt(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_120_split_fifty_fifty_AliceAndJohn_owe_40_each_toBob(self):
        # Arrange
        expected = 40
        expenses_made = 120
        friends = ["Bob", "Alice", "John"]

        # Act
        actual = compute_uniform_debt(expenses_made, friends)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_is_debitor_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice"]
        expected = {"Alice"}

        # Act
        actual = get_debtors(friends, payer)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_and_John_are_debtors_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice", "John"]
        expected = {"Alice", "John"}

        # Act
        actual = get_debtors(friends, payer)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_an_amount_Alice_John_and_Claire_are_debtors_to_Bob(self):
        # Arrange
        payer = "Bob"
        friends = ["Bob", "Alice", "John", "Claire"]
        expected = {"Alice", "John", "Claire"}

        # Act
        actual = get_debtors(friends, payer)

        # Assert
        self.assertEquals(expected, actual)

    def test_Bob_payed_20_for_Bob_and_Alice_and_Bob_payed_30_for_Bob_and_Alice_Alice_owes_25_to_Bob(self):
        # Arrange
        payments = [20, 30]
        payer = "Bob"
        friends = ["Bob", "Alice"]
        expected = {"Alice": 25}

        # Production
        debtor = get_debtors(friends, payer).pop()
        payments_amount = sum(payments)
        debt = compute_uniform_debt(payments_amount, friends)
        production = [{debtor: debt}]

        # Act
        debts_details = production

        # Assert
        self.assertIn(expected, debts_details)
