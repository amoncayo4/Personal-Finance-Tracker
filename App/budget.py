"""
=== Budget Methods ===
1. Budget(float, list, list, list, list)
2. add_transaction(float, str, str, str): void
3. get_total_spent(): float
4. get_transaction_choices(): list of tuples
5. get_remaining_budget(): float
6. add_category(str, float): void
7. get_category_by_name(str): Category
8. add_debt(str, float, floata): void
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
20. to_dict
21. save_to_file
22. from_dict
23. load_from_file
"""

# TODO: import the other classes
import json
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

    def add_transaction(self, amount, category_index_string, description, date):
        try:
            index = int(category_index_string)
            real_category_object = self.get_category_by_index(index)
            real_category_name = real_category_object.get_name()
        except:
            real_category_name = category_index_string

        new_transaction = Transaction(amount, real_category_name, description, date)
        self.__transactions.append(new_transaction)

    def add_transanction(self, amount, category_name, description, date):
        self.add_transaction(amount, category_name, description, date)

    """
    User Story 13.	View Total Spent: As a user, I need to see my total spent in a month so that I can track my overall spending.
    """
    # TODO: Create a get_total_spent method. This method will find the total spend from all transactions.

    def get_total_spent(self):
        total = 0
        for item in self.__transactions:
            total = total + item.get_amount()
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
        choices_list = []
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
        remaining = self.__monthly_income - total_spent

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
        return None

    """
    User Story 8. Add a Debt: As a user, I need to add a debt so that I can track what I owe.
    """
    # TODO: Create an add_debt method that will take in all the data to create a debt object then add it to the list of debts
    #       managed by the budget.

    def add_debt(self, name, total_amount, amount_paid=0):
        new_debt = Debt(name, total_amount)
        if amount_paid != 0:
            new_debt.set_amount_paid = (amount_paid)
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
        if current_amount != 0:
            new_fund.set_current_amount = (current_amount)
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

    def set_categories(self, categories_list):
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

    def update_debt_by_index(self, index, new_name, new_total_amount, new_amount_paid):
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
        return summary
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

    """
    The following four methods implement memory persistence—the idea of data persisting across runs. With these functions the same
    data will be loaded every time the application runs automatically, so you won't have to manually input the data every time 
    you want to test a function of the application. I felt so mean having you implement this so late.
    """
    # TODO: Write a method that will convert a Budget object to a dictionary. It should use the attribute names and values
    #       as the key-value pairs in the dictionary. Each attribute that is composed of other classes should also be converted
    #       to dictionary objects using their respective to_dict methods

    def to_dict(self):
        return {
            "monthly_income": self.__monthly_income,
            "categories": [c.to_dict() for c in self.__categories],
            "transactions": [t.to_dict() for t in self.__transactions],
            "debts": [d.to_dict() for d in self.__debts],
            "sinking_funds": [s.to_dict() for s in self.__sinking_funds],
        }

    # TODO: Add memory persistence by saving to a file. Open the specified filename from the parameter.
    #       Use json.dump to write the budget to the file as a dictionary.

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    # TODO: Write a method to convert a dictionary object into a budget object. This will be a static method which means it does 
    #       not need the self attribute. Put @staticmethod above the function definition to show this. This method should take in
    #       a dictionary as a parameter and populate a Budget object with the data from the dictionary. The dictionary keys 
    #       should be the same as the attributes for Budget. This should load the values for each attribute in a budget from the 
    #       corresponding key in the dictionary. The attributes that should be composed of other objects should call that object's
    #       respective from_dict method.
    @staticmethod
    def from_dict(data):
        budget = Budget()
        budget.set_monthly_income(data.get("monthly_income", 0))

        budget.set_categories([Category.from_dict(c) for c in data.get("categories", [])])
        budget.set_transactions([Transaction.from_dict(t) for t in data.get("transactions", [])])
        budget.set_debts([Debt.from_dict(d) for d in data.get("debts", [])])
        budget.set_sinking_funds([Sinking_Fund.from_dict(s) for s in data.get("sinking_funds", [])])

        return budget

    # TODO: Write a load_from_file method that takes a file name passed in the parameters. It should then use json.load to read
    #       the contents of the file. The data read from the file should then be converted to objects from the dictionary contents.
    #       This will also be a static function.
    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            return Budget.from_dict(data)
        except Exception as e:
            print(f"Failed to load {e}")
            print(f"Trying to load {filename}")
            return Budget()

    # TODO: Write a rollever method that is a static method. It will be passed a previous Budget object. It will take the following
    #       values from the previous budget and set the corresponding attributes on the current budget:
    #           - monthly_income
    #           - categories and all their attributes
    #           - sinking funds keeping their goal amount and progress
    #           - debts keeping their owed amount and progress
    #       The function will then return the newly created budget with values rolled over from the prvious month.
    @staticmethod
    def rollover(prev_budget):
        new_budget = Budget()

        new_budget.set_monthly_income(prev_budget.get_monthly_income())
        new_budget.set_categories(prev_budget.get_categories())
        new_budget.set_debts(prev_budget.get_debts())
        new_budget.set_sinking_funds(prev_budget.get_sining_funds())

        return new_budget