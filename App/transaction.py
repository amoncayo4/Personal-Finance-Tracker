"""
=== Transaction Methods ===
1. Constructor(float, str, str, str)
getters and setters
"""

# TODO: Create a Transaction class with the attributes amount, category_name, description, and date. All attributes should be
#       declared as private.

class Transaction:
    def __init__(self, amount, category_name, description, date):
        self.__amount = amount
        self.__category_name = category_name
        self.__description = description
        self.__date = date

    # TODO: Write getters and setters for all attributes (4 getters and 4 setters)

    def get_Amount(self):
        return self.__amount

    def get_category_name(self):
        return self.__category_name

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def set_amount(self, amount):
        self.__amount = amount

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def set_description(self, description):
        self.__description = description

    def set_date(self, date):
        self.__date = date