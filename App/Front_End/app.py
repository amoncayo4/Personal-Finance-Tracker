from flask import Flask, render_template, request, redirect, url_for
from budget import Budget
from transaction import Transaction
from sinking_fund import Sinking_Fund
from debt import Debt

app = Flask(__name__)

budget = Budget()

@app.route('/')
def home():
    categories = budget.get_categories()
    transactions = budget.get_transactions()
    sinking_funds = budget.get_sinking_funds()
    debts = budget.get_debts()
    return render_template(
        'home.html',
        categories=categories,
        transactions=transactions,
        sinking_funds=sinking_funds,
        debts=debts
    )

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        limit = float(request.form['budget_limit'])
        budget.add_category(name, limit)
        return redirect(url_for('home'))
    return render_template('add_category.html')

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        budget.add_transaction(amount, category, description, date)
        return redirect(url_for('home'))
    categories = budget.get_categories()
    return render_template('add_transaction.html', categories=categories)

@app.route('/add_sinking_fund', methods=['GET', 'POST'])
def add_sinking_fund():
    if request.method == 'POST':
        name = request.form['name']
        goal = float(request.form['goal'])
        budget.add_sinking_fund(name, goal, 0)
        return redirect(url_for('home'))
    return render_template('add_sinking_fund.html')

@app.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    if request.method == 'POST':
        name = request.form['name']
        total = float(request.form['total'])
        budget.add_debt(name, total, 0)
        return redirect(url_for('home'))
    return render_template('add_debt.html')

if __name__ == '__main__':
    app.run(debug=True)
