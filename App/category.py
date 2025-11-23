"""
=== Category Methods ===
1. Constructor(str, float)
2. get_spent_amount
3. to_dict
4. from_dict
getters and setters
"""

# TODO: Create a Category class with the attributes name and budget_limit. All attributes should be declared as private. 
class Category:

    def __init__(self, name, budget_limit):
        self.__name = name
        self.__budget_limit = budget_limit
    # TODO: Write getters and setters for all attributes (2 getters and 2 setters)

    def get_name(self):
        return self.__name

    def get_budget_limit(self):
        return self.__budget_limit

    def set_name(self, name):
        self.__name = name

    def set_budget_limit(self, budget_limit):
        self.__budget_limit = budget_limit



    """
    This is a helper function for finding the category summaries
    """
    # TODO: Create a get_spent_amount method that uses a list of transactions to find the total spent from transactions in a certain category.
<<<<<<< HEAD


    def get_spent_amount(self, all_transactions):
        total_spent = 0
        for transaction in all_transactions:
            if transaction.get_category() == self.__name:
                total_spent = total_spent + transaction.get_Amount()

        return total_spent
=======
    
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.

    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Category object.
>>>>>>> upstream/main
