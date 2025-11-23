"""
=== Transaction Methods ===
1. Constructor(float, str, str, str)
2. get_spent_amount
3. to_dict
4. from_dict
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

    def get_amount(self):
        return self.__amount

    def get_category(self):
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

    # TODO: Write getters and setters for all attributes (4 getters and 4 setters)

    """
    This will be a helper function for memory persistence (file usage to store data)
    """

    def to_dict(self):
        return {
            "amount": self.__amount,
            "category_name": self.__category_name,
            "description": self.__description,
            "date": self.__date
        }

    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    @staticmethod
    def from_dict(data):
        return Transaction(
            data["amount"],
            data["category_name"],
            data["description"],
            data["date"]
        )

    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Transaction object.
