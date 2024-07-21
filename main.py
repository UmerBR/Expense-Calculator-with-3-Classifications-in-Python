import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt

class Expense:
    def __init__(self, amount, name, date=None):
        self.amount = amount
        self.name = name
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"${self.amount} on {self.date} for {self.name}"

class Necessity(Expense):
    category = "necessity"

class Comfort(Expense):
    category = "comfort"

class Luxury(Expense):
    category = "luxury"

class ExpenseTracker:
    def __init__(self):
        self.categories = {
            Necessity.category: [],
            Comfort.category: [],
            Luxury.category: []
        }

    def add_expense(self, expense):
        if expense.category in self.categories:
            self.categories[expense.category].append(expense)
            messagebox.showinfo("Success", f"Added {expense.category} expense: {expense}")
        else:
            messagebox.showerror("Error", f"Invalid category: {expense.category}")

    def view_expenses(self, category=None):
        if category and category not in self.categories:
            messagebox.showerror("Error", f"Invalid category. Choose from {list(self.categories.keys())}")
            return
        
        expenses_text = ""
        if category:
            expenses_text += f"Expenses in category '{category}':\n"
            for expense in self.categories[category]:
                expenses_text += str(expense) + "\n"
        else:
            for cat, expenses in self.categories.items():
                expenses_text += f"Expenses in category '{cat}':\n"
                for expense in expenses:
                    expenses_text += str(expense) + "\n"
                expenses_text += "\n"

        self.display_text(expenses_text)

    def analyze_expenses(self):
        analysis_text = "Expense Analysis:\n"
        for category, expenses in self.categories.items():
            total = sum(expense.amount for expense in expenses)
            analysis_text += f"Total spent on {category}: ${total:.2f}\n"

        self.display_text(analysis_text)

    def display_text(self, text):
        display_window = tk.Toplevel()
        display_window.title("Display")
        display_window.geometry("600x400")
        text_widget = tk.Text(display_window, wrap='word')
        text_widget.insert(tk.END, text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill='both')

    def plot_line_graph(self):
        dates = []
        amounts = []
        for expenses in self.categories.values():
            for expense in expenses:
                dates.append(datetime.strptime(expense.date, "%Y-%m-%d"))
                amounts.append(expense.amount)

        if not dates:
            messagebox.showinfo("Info", "No expenses to plot.")
            return

        dates, amounts = zip(*sorted(zip(dates, amounts)))
        
        plt.figure()
        plt.plot(dates, amounts, marker='o')
        plt.title("Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.grid(True)
        plt.show()

    def plot_pie_chart(self):
        categories = []
        amounts = []
        for category, expenses in self.categories.items():
            total = sum(expense.amount for expense in expenses)
            if total > 0:
                categories.append(category)
                amounts.append(total)

        if not categories:
            messagebox.showinfo("Info", "No expenses to plot.")
            return

        plt.figure()
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title("Expenses by Category")
        plt.show()

def main():
    def add_expense():
        amount = amount_entry.get()
        name = name_entry.get()
        date = date_entry.get()
        category_choice = category_var.get()

        if not amount or not name or category_choice == "Select":
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        amount = float(amount)
        date = date if date else None

        if category_choice == "Necessity":
            expense = Necessity(amount, name, date)
        elif category_choice == "Comfort":
            expense = Comfort(amount, name, date)
        elif category_choice == "Luxury":
            expense = Luxury(amount, name, date)

        tracker.add_expense(expense)

    def view_expenses():
        category_choice = category_var.get().lower()
        category_choice = category_choice if category_choice != "Select" else None
        tracker.view_expenses(category_choice)

    def analyze_expenses():
        tracker.analyze_expenses()

    tracker = ExpenseTracker()
    root = tk.Tk()
    root.title("Expense Tracker")
    root.state('zoomed')  # Maximize window on startup

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both', pady=50)

    # Add Expense Section
    tk.Label(main_frame, text="Add Expense").pack(pady=5)
    
    amount_frame = tk.Frame(main_frame)
    amount_frame.pack(pady=5)
    tk.Label(amount_frame, text="Amount:").pack(side='left')
    amount_entry = tk.Entry(amount_frame)
    amount_entry.pack(side='left')

    name_frame = tk.Frame(main_frame)
    name_frame.pack(pady=5)
    tk.Label(name_frame, text="Name:").pack(side='left')
    name_entry = tk.Entry(name_frame)
    name_entry.pack(side='left')

    date_frame = tk.Frame(main_frame)
    date_frame.pack(pady=5)
    tk.Label(date_frame, text="Date (YYYY-MM-DD):").pack(side='left')
    date_entry = tk.Entry(date_frame)
    date_entry.pack(side='left')

    category_frame = tk.Frame(main_frame)
    category_frame.pack(pady=5)
    tk.Label(category_frame, text="Category:").pack(side='left')
    category_var = tk.StringVar(value="Select")
    category_menu = tk.OptionMenu(category_frame, category_var, "Necessity", "Comfort", "Luxury")
    category_menu.pack(side='left')

    add_button = tk.Button(main_frame, text="Add Expense", command=add_expense)
    add_button.pack(pady=5)

    # View Expenses Section
    view_button = tk.Button(main_frame, text="View All Expenses", command=view_expenses)
    view_button.pack(pady=5)

    # Analyze Expenses Section
    analyze_button = tk.Button(main_frame, text="Analyze Expenses", command=analyze_expenses)
    analyze_button.pack(pady=5)

    # Plot Line Graph Section
    line_graph_button = tk.Button(main_frame, text="Plot Line Graph", command=tracker.plot_line_graph)
    line_graph_button.pack(pady=5)

    # Plot Pie Chart Section
    pie_chart_button = tk.Button(main_frame, text="Plot Pie Chart", command=tracker.plot_pie_chart)
    pie_chart_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
