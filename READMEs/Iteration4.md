# Semester Project: Money Management System  
## Iteration 4 – Data Operations Implementation  

## Warning:  
Do not change anything in `main.py`, `app.py`, or the `Front_End` directory.  
Don't touch my front end >:(  

---

### System Description  
This iteration expands the *Money Management System* by adding full backend functionality for **data operations**.  
Where Iteration 3 focused on creating the classes and enabling basic “add” features, this phase implements the logic needed to **update**, **delete**, and **summarize** information already stored in the system.  

You will now write the backend code that supports every major action in the interface — **Add**, **Edit**, and **Delete** — for transactions, debts, categories, and sinking funds.  
These additions allow the program to actively manage its data, completing the transition from a simple data holder to a functional personal-finance tool.  

All changes should be made in the backend Python files.  
The Flask front end has already been configured to call these new backend methods automatically once implemented.  

---

### Deliverables  
You are responsible for completing the **TODOs** provided in the project files.  
Each TODO marks a required step to make data operations work for the corresponding feature.

| File | Number of TODOs |
|------|----------------:|
| `budget.py` | 8 |
| `debt.py` | 2 |
| `category.py` | 1 |
| `sinking_fund.py` | 3 |
| **Total** | **14** |

Use PyCharm’s **TODO tool window** to keep track of your progress.  
As you finish each one, replace `TODO` with `DONE` to confirm completion and avoid missing any steps.  

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
Once the application is running, test all front-end buttons and pages:  

- **Transactions –** Add, Edit, and Delete transactions.  
- **Categories –** Add categories and view their spending summaries.  
- **Debts –** Add debts, make payments, and verify updated balances.  
- **Sinking Funds –** Add contributions, view progress, and delete funds.  

If every button (Add, Edit, Delete) functions correctly and the displayed information updates immediately without errors, your backend implementation for Iteration 4 is complete.  

---

### Submitting Your Work  
To push your work to your GitHub repository, open the terminal in the project directory and run:  
```
git add .
git commit -m "Solution for Iteration 4"
git push
```
