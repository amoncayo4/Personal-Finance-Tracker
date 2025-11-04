# Semester Project: Money Management System  
## Iteration 3 – Backend Implementation  

## Warning: 
Do not change anything in main.pu, app.py, or the Front_End directory. Don't touch my front end >:(.

### System Description  
This iteration transitions the *Money Management System* from design to implementation. You will now begin writing the **backend code** that powers the system you previously modeled in your **UML diagrams and User Stories**.  

The program runs locally on your computer using **Flask**, which hosts the application on your machine rather than on the web. It supports a single user and brings together all parts of the financial system—transactions, categories, debts, and sinking funds—into a working budget manager.  

The front end is completed for you; your job is to work on the backend functionality for those components. The tasks you complete here connect directly to the user stories provided in Iteration 2. Completing these TODOs will demonstrate how your original design decisions translate into working software, showing the clear link between the **design phase** and **development phase** of the project.  

---

### Deliverables  
You are responsible for completing the TODOs provided in the project files.  
Each TODO marks a place where code must be added to complete a portion of the backend system.  

| File | Number of TODOs |
|------|-----------------|
| `budget.py` | 12 |
| `transaction.py` | 2 |
| `category.py` | 2 |
| `debt.py` | 2 |
| `sinking_fund.py` | 2 |

Use PyCharm’s **TODO tool window** to keep track of your progress.  
As you finish each one, replace `TODO` with `DONE`. This helps confirm your progress and makes sure no steps are missed.  

---

### Running the Application  
To run the program:  
1. Open the project in **PyCharm**.  
2. Run the main Flask file.  
3. In the terminal, you should see output similar to the following:  
   ![Running Terminal](running_terminal.png)  
4. In your terminal, click the `http://127.0.0.1:5000` link to open the app in your browser.  
      

---

### Verifying Your Work  
Once the application is running, you should be able to interact with all four areas of the system:  
- **Transactions** – Add new transactions and view them in the list.  
- **Categories** – Add categories and confirm they appear correctly.  
- **Debts** – Add new debts and verify that payment and balance data display properly.  
- **Sinking Funds** – Add funds and check that their progress updates correctly.  

If all four areas can successfully **add** and **display** information without errors, your backend should be functioning correctly.  

---

### Submitting your work

To push your work to the GitHub repository, open your terminal to the project directory and run the commands:
```
git add .
git commit -m "Solution for Iteration 3"
git push
```
