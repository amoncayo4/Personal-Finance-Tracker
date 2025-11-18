"""
=== Budget Methods ===
1. Budget(float, list, list, list, list)
2. add_transaction(float, str, str, str): void
3. get_total_spent(): float
4. get_transaction_choices(): list of tuples
5. get_remaining_budget(): float
6. add_category(str, float): void
7. get_category_by_name(str): Category
8. add_debt(str, float, float): void
9. get_debt_choices(): list of tuples
10. add_sinking_fund(str, float, float): void
11. get_fund_choices(): list of tuples
12. get_transaction_by_index
13. delete_transaction_by_index
14. get_debt_by_index
15. delete_debt_by_index
16. get_sinking_fund_by_index
17. delete_sinking_fund_by_index
18. get_summary_by_category
19. get_category_summary
"""
from operator import index

# TODO: import the other classes

from transaction import Transaction
from category import Category
from debt import Debt
from sinking_fund import Sinking_Fund

# TODO: Create a Budget class with the attributes monthly_income, categories, transactions, sinking_funds, and debts.
#       All attributes should be declared as private. The monthly_income should be set to 0 and the others should be empty lists.

class Budget:
    def __init__(self):
        self.__monthly_income = 0
        self.__categories = []
        self.__transactions = []
        self.__sinking_funds = []
        self.__debts = []
    """
    User Story 2.	Add a Transaction: As a user, I need to add a transaction so that I can record my spending.
    """
    # TODO: Create an add_transaction method. It will take in the information to make a transaction object then add
    #       it to the list of transactions managed by the budget

    def add_transaction(self, amount, category_name, description, date):
        new_transaction = Transaction(amount, category_name, description, date)

        self.__transactions.append(new_transaction)

    """
    User Story 13.	View Total Spent: As a user, I need to see my total spent in a month so that I can track my overall spending.
    """
    # TODO: Create a get_total_spent method. This method will find the total spend from all transactions.

    def get_total_spent(self):
        total = 0
        for item in self.__transactions:
            total = total + item.get_amount

        return total

    """
    User Story As a user, I need to view all my transactions so that I can review past activity.
    """
    # TODO: Create a get_transaction_choices method. It will return a list of tuples with the number of the transaction 
    #       and the formatted transaction data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuples should be formatted as such:
    #       (number of transaction, "date - description ($amount) in category")
    #       The amount should print two decimal places.

    def get_transaction_choices(self):
        choices = []

        for index, trans in enumerate(self.__transactions):
            date = trans.get_date()
            desc = trans.get_description()
            amount = trans.get_amount()
            cat = trans.get_category()
            formatted_string = f"{date} - {desc} (${amount:.2f}) in {cat}"
            choice_tuple = (index, formatted_string)
            choices_list.append(choice_tuple)

        return choices_list

    """"
    User Story 14.	See Remaining Budget: As a user, I need to see my remaining budget so that I can avoid overspending.
    """
    # TODO: Create a get_remaining_budget method. This will find the difference between the monthly income and the amount already spent.

    def get_remaining_budget(self):
        total_spent = self.get_total_spent()

        remaining = self.__monthly_income = total_spent
        return remaining

    """
    User Story 4. Add a Category: As a user, I need to add a category so that I can organize my transactions.
    """
    # TODO: Create an add_category method that will take in all the data to create a category object then add it 
    #       to the list of categories managed by the budget.

    def add_category(self, name, budget_limit):
        new_category = Category(name, budget_limit)
        self.__categories.append(new_category)

    """
    This will be used in a later function to retrieve a desired category.
    """
    # TODO: Create a get_category by name method. This will retrieve the category object from the list of categories by 
    #       searching for the entry with the same name as the string given to the function.

    def get_category_by_name(self, name_to_find):
        for category in self.__categories:
            if category.get_name() == name_to_find:
                return category

        return none

    """
    User Story 8. Add a Debt: As a user, I need to add a debt so that I can track what I owe.
    """
    # TODO: Create an add_debt method that will take in all the data to create a debt object then add it to the list of debts
    #       managed by the budget.

    def add_debt(self, name, total_amount, amount_paid):
        new_debt = Debt(name, total_amount)
        self.__debts.append(new_debt)

    """
    This will be used in a later function to retrieve a desired debt.
    """
    # TODO: Create a get_debt_choices method. This method will return a list of tuples with the number of the debt
    #       and the formatted debt data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Paid $paid / $total")
    #       The paid and total should print two decimal places.

    def get_debt_choices(self):
        choices_list = []

        for index, debt in enumerate(self.__debts):
            name = debt.get_name()
            paid = debt.get_amount_paid()
            total = debt.get_total_amount()

            formatted_string = f"{name}: Paid ${paid:.2f} / ${total:.2f}"
            choice_tuple = (index, formatted_string)
            choices_list.append(choice_tuple)
        return choices_list

    """
    User Story 11. Add a Sinking Fund: As a user, I need to add a sinking fund so that I can save toward specific goals.
    """
    # TODO: Create an add_sinking_fund method that will take in all the data to create a sinking fund object then add it to 
    #       the list of sinking funds managed by the budget. 

    def add_sinking_fund(self, name, goal_amount, current_amount):
        new_fund = Sinking_Fund(name, goal_amount)
        self.__sinking_funds.append(new_fund)

    """
    This will be used in a later function to retrieve a desired sinking fund.
    """
    # TODO: Create a get_fund_choices method. This method will return a list of tuples with the number of the sinking fund
    #       and the formatted sinking fund data. The list will be made by extracting all the data from each object and turning
    #       it into a formatted string object. That object should be enumerated, then placed into a tuple object with the number.
    #       The tuple should be formatted as such: 
    #       (number of debt, "name: Saved $saved / $goal")
    #       The saved and goal should print two decimal places.

    def get_fund_choices(self):
        choices_list = []

        for index, fund in enumerate(self.__sinking_funds):
            name = fund.get_name()
            saved = fund.get_current_amount()
            goal = fund.get_goal_amount()
            formatted_string = f"{name}: Saved ${saved:.2f} / ${goal:.2f}"
            choice_tuple = (index, formatted_string)
            choices_list.append(choice_tuple)
        return choices_list

    # TODO: Write getters and setters for each of the attributes (5 getters and 5 setters)

    def get_monthly_income(self):
        return self.__monthly_income

    def get_categories(self):
        return self.__categories

    def get_transactions(self):
        return self.__transactions

    def get_sinking_funds(self):
        return self.__sinking_funds

    def get_debts(self):
        return self.__debts


    def set_monthly_income(self, amount):
        self.__monthly_income = amount

    def set_categories(self, amount):
        self.__monthly_income = amount

    def set_categories(self, amount):
        self.__categories = categories_list

    def set_transactions(self, transactions_list):
        self.__transactions = transactions_list

    def set_sinking_funds(self, funds_list):
        self.__sinking_funds = funds_list

    def set_debts(self, debts_list):
        self.__debts = debts_list

    """
    This will be a helper function for deleting and editing a transaction
    """
    # TODO: Create a get_transaction_by_index method that will take in an index number and return the transaction
    #       object stored at that position in the list of transactions.

    def get_transaction_by_index(self, index):
        return self.__transactions[index]

    """
    User Story 16. Delete a Transaction: As a user, I need to delete a transaction so that I can remove mistakes.
    """
    # TODO: Create a delete_transaction_by_index method. This method will take in an index number and remove the
    #       transaction object at that position from the list of transactions.

    def delete_transaction_by_index(self, index):
        self.__transactions.pop(index)

    """
    This will be a helper function for deleting and editing a debt
    """

    def update_transaction_by_index(self, index, new_amount, new_category_name, new_description, new_date):
        transaction = self.__transactions[index]
        transaction.set_amount(new_amount)
        transaction.set_category(new_category_name)
        transaction.set_description(new_description)
        transaction.set_date(new_date)


    # TODO: Create a get_debt_by_index method that will take in an index number and return the debt
    #       object stored at that position in the list of debts.

    def get_debt_by_index(self, index):
        return self.__debts[index]

def update_debt_by_index(self, index. new_name. new_total_amount, new_amount_paid):
    debt = self.__debts[index]
    debt.set_name(new_name)
    debt.set_total_amount(new_total_amount)
    debt.set_amount_paid(new_amount_paid)



    """
    User Story 17. Delete a Debt: As a user, I need to delete a debt so that I can remove a fully paid or incorrect one.
    """
    # TODO: Create a delete_debt_by_index method. This method will take in an index number and remove the
    #       debt object at that position from the list of debts.

    def delete_debt_by_index(self, index):
        self.__debts.pop(index)

    """
    This will be a helper function for deleting and editing a sinking fund
    """

    def get_category_by_index(self, index):
        return self.__categories[index]

    # TODO: Create a get_sinking_fund_by_index method that will take in an index number and return the sinking fund
    #       object stored at that position in the list of sinking funds.

    def get_sinking_funds_by_index(self, index):
        return self.__sinking_funds[index]

    """
    User Story 18. Delete a Sinking Fund: As a user, I need to delete a sinking fund so that I can remove old or irrelevant ones.
    """
    # TODO: Create a delete_sinking_fund_by_index method. This method will take in an index number and remove the
    #       sinking fund object at that position from the list of sinking funds.

    def delete_sinking_funds_by_index(self, index):
        return self.__sinking_funds[index]

    """
    This will be a helper function for deleting and editing a category
    """
    # TODO: Create a get_summary_by_category method. This method will build a dictionary containing the total amount
    #       spent for each category. It should loop through every category in the list and calculate its total by calling
    #       the category’s get_spent_amount method. The resulting dictionary should use the category name as the key and
    #       the total amount spent as the value.

    def get_summary_by_category(self):
        summary = {}

        for category in self.__categories:
            category_name = category.get_name()
            total_spent = category.get_spent_amount(self.__transactions)
            summary[category_name] = total_spent

    """
    User Story 5. View Spending by Category: As a user, I need to view spending by category so that I can see where my money goes.
    """
    # TODO: Create a get_category_summary method. This method will take in a category name and return a dictionary
    #       containing all spending information related to that category. It should find all transactions that match
    #       the category name, total their amounts, and include each transaction’s details (amount, description, and date).
    #       The returned dictionary should include:
    #           - "category": the category name
    #           - "total": total amount spent in that category
    #           - "limit": the category’s budget limit
    #           - "transactions": a list of dictionaries containing each transaction’s details

    def get_category_summary(self, category_name):
        category_object = self.get_category_by_name(category_name)

        if category_object is None:
            return None

        total = 0
        transactions_in_this_category = []

        for trans in self.__transactions:
            if trans.get_category() == category_name:
                total = total + trans.get_amount()

                trans_details = {
                    "amount": trans.get_amount(),
                    "description": trans.get_description(),
                    "date": trans.get_date(),
                }
                transactions_in_this_category.append(trans_details)


            summary = {
                "category": category_name,
                "total": total,
                "limit": category_object.get_budget_limit(),
                "transactions": transactions_in_this_category
            }
            return summary