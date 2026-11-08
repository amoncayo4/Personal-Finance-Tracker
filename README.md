# Personal Budgeting System

A Flask web app for tracking personal finances: budgets by category, transactions, debts and savings goals, with data saved to JSON. Built as a team project for CSC 2310 at Tennessee Tech, through an iterative process that went from user stories and UML design to a full object-oriented implementation.

## Features

- **Budgeting by category:** shows total spent and remaining budget for each category.
- **Transaction tracking:** log income and expenses with descriptions, dates and categories.
- **Debt tracking:** record payments against balances and see what's left.
- **Sinking funds:** track progress toward savings goals.
- **Monthly rollover:** each month is saved to its own JSON file, and a new month starts from the previous month's budget automatically.

## Tech

- Python, Flask and Jinja templates
- JSON file storage
- Object-oriented design with Budget, Transaction, Category, Debt and SinkingFund classes

## Project structure

```
App/
  main.py                 Starts the Flask app
  budget.py               Core budget logic and JSON save/load
  category.py             Category class
  transaction.py          Transaction class
  debt.py                 Debt class
  sinking_fund.py         Sinking fund class
  Front_End/app.py        Flask routes
  Front_End/Templates/    HTML templates
  Data/                   Monthly budget files (sample data)
Design/                   UML diagrams and iteration materials
user_stories.md           User stories
```

## Run it locally

```
git clone https://github.com/amoncayo4/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker/App
pip install flask
python main.py
```

Then open http://127.0.0.1:5000 in your browser.

The app reads its session key from the `FLASK_SECRET_KEY` environment variable and generates a random one if it isn't set.
