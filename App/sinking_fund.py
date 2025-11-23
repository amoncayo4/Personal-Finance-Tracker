"""
=== Sinking Fund Methods ===
1. Constructor(str, float, float)
2. add_contribution
3. get_progress
4. get_percent_saved
5. to_dict
6. from_dict
getters and setters
"""

# TODO: Create a Sinking_Fund class with the attributes name, goal_amount, and current_amount. All attributes should be 
#       declared as private. The current amount should be automatically set to $0.

class Sinking_Fund:
    def __init__(self, name, goal_amount):
        self.__name = name
        self.__goal_amount = goal_amount
        self.__current_amount = 0

    # TODO: Write getters and setters for all attributes (3 getter and 3 setters)

    def get_name(self):
        return self.__name

    def get_goal_amount(self):
        return self.__goal_amount

    def get_current_amount(self):
        return self.__current_amount

    def set_name(self, new_name):
        self.__name = new_name

    def set_goal_amount(self, new_goal):
        self.__goal_amount = new_goal

    def set_current_amount(self, new_amount):
        self.__current_amount = new_amount

    """
    User Story 12.	Track Fund Contribution: As a user, I need to track a contribution to my sinking fund so that I can grow the fund.
    """
    # TODO: Create an add_contribution method which accepts an amount of money the user is adding to the total saved

    def add_contribution(self, contribution_amount):
        self.__current_amount = self.__current_amount + contribution_amount

    """
    Used in get_percent_saved()
    """
    # TODO: Create a get_progress method to help the get_percent_saved method

    def get_progress(self):
        if self.__goal_amount == 0:
            return 0

        progress = self.__current_amount / self.__goal_amount
        return progress

    """
    User Story 19.	View Percent Paid: As a user, I need to see the percent saved of my sinking fund so that I know how close I am to my goal.
    """
    # TODO: Create a get_percent_saved method to calculate what percent of the goal has been saved

    def get_percent_saved(self):
        percent = self.get_progress() * 100
        return percent
    
    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a to_dict method that will turn an object into a dictionary using the attribute names and values as key-value pairs.

    def to_dict(self):
        return {
            "name": self.__name,
            "goal_amount": self.__goal_amount,
            "current_amount": self.__current_amount,
        }

    """
    This will be a helper function for memory persistence (file usage to store data)
    """
    # TODO: Write a from_dict method that will use a dictionary parameter to create and return a Sinking Fund object.
    def from_dict(data):
        fund = Sinking_Fund(data["data"], data["goal_amount"])
        fund.set_current_amount(data["current_amount"])

        return fund