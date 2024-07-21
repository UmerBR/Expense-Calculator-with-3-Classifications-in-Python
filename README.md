#Expense Tracker

This is a Python-based Expense Tracker application with a graphical user interface (GUI) built using tkinter. It allows users to add, view, and analyze their expenses, and also provides graphical representations of expenses using line graphs and pie charts.

##**Features**
Add Expenses: Add expenses with amount, name, date, and category.
View Expenses: View expenses by category or view all expenses.
Analyze Expenses: Analyze total expenses by category.
Graphical Representations:
Line graph of expenses over time.
Pie chart of expenses by category.
Prerequisites
Make sure you have Python installed. You can download it from python.org.

##**Installation**
Clone this repository or download the source code.

Install the required library matplotlib:

```
pip install matplotlib
```

##**Usage**

Run the expense_tracker.py file:

```
python expense_tracker.py
```

The application will open in a maximized window.

Use the following features in the application:

**Add Expense: **
Fill in the amount, name, date, and select a category, then click the "Add Expense" button.
**View All Expenses: **
Click the "View All Expenses" button to see a list of all expenses.
**Analyze Expenses: **
Click the "Analyze Expenses" button to get a summary of total expenses by category.
**Plot Line Graph: **
Click the "Plot Line Graph" button to see a line graph of expenses over time.
**Plot Pie Chart: **
Click the "Plot Pie Chart" button to see a pie chart of expenses by category.


##**Code Overview**

**Expense Classes**
###Expense: 
Base class representing an expense with amount, name, and date.
###Subclasses of Expense: 
Necessity, Comfort, Luxury representing different categories of expenses.
Expense Tracker Class
###ExpenseTracker: 
Manages the expenses, allowing addition, viewing, and analysis of expenses. Also handles plotting graphs.
###GUI Implementation:
The main function initializes the tkinter GUI, creating input fields and buttons for the user to interact with the application.
###Graphical Representation:
plot_line_graph: Plots a line graph of expenses over time.
plot_pie_chart: Plots a pie chart of expenses by category.


##**Example**

###Adding an Expense:

Enter the amount.
Enter the name of the expense.
Enter the date in YYYY-MM-DD format (leave blank for today's date).
Select a category (Necessity, Comfort, or Luxury).
Click "Add Expense".

###Viewing Expenses:

Click "View All Expenses" to see all expenses listed by category.

###Analyzing Expenses:

Click "Analyze Expenses" to get a total of expenses by category.

###Plotting Graphs:

Click "Plot Line Graph" to visualize expenses over time.
Click "Plot Pie Chart" to visualize expenses by category.

**License**

This project is licensed under the MIT License.

