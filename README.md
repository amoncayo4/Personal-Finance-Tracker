#Personal Budgeting System

A backend focused financial management application built with Python. This project was developed through a iteration software development cycle, moving from requirement gathering to a full Object-Oriented implementation.

#Project Overview
This program allows users to record and track personal finances over time. It provides a view of financials by managing daily spending, comparing activity against budget limits, and monitoring debt and savings progress.

#Language: Python
#Framework: Flask (Local Web Hosting)
#Data Storage:JSON
#Methodology: Object-Oriented Programming (OOP) and Iterative Design

#Features
Automated Budgeting: Calculates total spent vs. remaining budget by category to prevent overspending.
Transaction Tracking: Logging of income and expenses with descriptions, dates, and category mapping.
Debt Management: Tracks total balances and records payments to calculate remaining dues.
Sinking Funds: Monitors progress toward savings targets.
Data Persistence: Implemented logic to save and load user profiles automatically.

#Design
This project prioritizes clean, maintainable code through design artifacts located in the Documentatio folder
User Stories: Captured user needs following the format: "As a <user>, I want <feature> so that <benefit>".
UML Class Diagram: Mapped the system architecture, including classes for Budget, Transaction, Category, Debt, and Sinking_Fund.

# Project Structure
app.py - Flask entry point and front-end integration.
budget.py - Backend logic and data management.
Classes - Individual class definitions for financial objects.
Tests - Unit tests to verify backend calculations.
Documentation - UML diagrams, user stories, and iteration logs.

# Setup & Installation
1. Clone the repository: git clone https://github.com/amoncayo4/Personal-Finance-Tracker.git
2. Ensure Python and Flask are installed.
3. Run main.py to host the application locally 
