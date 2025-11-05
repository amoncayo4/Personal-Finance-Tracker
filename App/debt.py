"""
=== Debt Methods ===
1. Constructor(str, float)
2. make_payment
3. get_remaining_balance
getters and setters
"""
from tkinter.font import names


# TODO: Create a Debt class with the attributes name, total_amount, and amount, paid. All attributes should be declared as private.
#       The amount paid should be automatically declared as $0.

class Debt:

    def __init__(self, name, total_amount):
        self.__name = name
        self.__total_amount = total_amount
        self.__amount_paid = 0

    # TODO: Write getters and setters for all attributes (3 getters and 3 setters)

    def get_name(self):
        return self.__name

    def get_total_amount(self):
        return self.__total_amount

    def get_amount_paid(self):
        return self.__amount_paid

    def set_name(self, new_name):
        self.__name = new_name

    def set_total_amount(self, new_total):
        self.__total_amount = new_total

    def set_amount_paid(self, new_amount_paid):
        self.__amount_paid = new_amount_paid


    """
    User Story 9. Track a Debt Payment: As a user, I need to track a payment to my debt so that I can reduce my balance.
    """
    # TODO: Create a make_payment method to accept the amount the of money the user is paying and apply it to the amount paid

    def make_payment(self, payment_amount):
        self.__amount_paid = self.__amount_paid + payment_amount

    """
    User Story 10. View Remaining Balance: As a user, I need to see the remaining balance for my debt so that I know what’s left to pay.
    """
    # TODO: Create a get_remaining_balance method to calculate how much of the debt is left to be paid

    def get_remaining_balance(self):
        remaining = self.__total_amount - self.__amount_paid
        return remaining