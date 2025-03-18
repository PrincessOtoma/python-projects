import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.transactions = []

        # Input Section
        tk.Label(root, text="Category:").grid(row=0, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(root)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Transaction", command=self.add_transaction).grid(row=3, column=0, columnspan=2, pady=10)

        # Transaction List
        self.transaction_list = ttk.Treeview(root, columns=("Category", "Amount", "Date"), show="headings")
        self.transaction_list.heading("Category", text="Category")
        self.transaction_list.heading("Amount", text="Amount")
        self.transaction_list.heading("Date", text="Date")
        self.transaction_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Delete Button
        tk.Button(root, text="Delete Selected Transaction", command=self.delete_transaction).grid(row=5, column=0, columnspan=2, pady=10)

        # Summary Section
        self.summary_label = tk.Label(root, text="Total Income: $0.00 | Total Expenses: $0.00 | Balance: $0.00")
        self.summary_label.grid(row=6, column=0, columnspan=2, pady=10)

        # Filter Section
        tk.Label(root, text="Filter by Category:").grid(row=7, column=0, padx=10, pady=10)
        self.filter_category = ttk.Combobox(root, values=["All"])
        self.filter_category.grid(row=7, column=1, padx=10, pady=10)
        self.filter_category.set("All")
        self.filter_category.bind("<<ComboboxSelected>>", self.filter_transactions)

    def add_transaction(self):
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()

        # Input Validation
        if not category or not amount or not date:
            messagebox.showerror("Error", "All fields are required!")
            return
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return

        # Add Transaction
        transaction = {"category": category, "amount": amount, "date": date}
        self.transactions.append(transaction)
        self.update_transaction_list()
        self.update_summary()
        self.clear_inputs()

    def delete_transaction(self):
        selected_item = self.transaction_list.selection()
        if not selected_item:
            messagebox.showerror("Error", "No transaction selected!")
            return

        # Get the selected transaction's index
        selected_index = self.transaction_list.index(selected_item)
        del self.transactions[selected_index]

        # Update UI
        self.update_transaction_list()
        self.update_summary()

    def update_transaction_list(self):
        # Clear existing rows
        for row in self.transaction_list.get_children():
            self.transaction_list.delete(row)

        # Add transactions to the list
        for transaction in self.transactions:
            self.transaction_list.insert("", "end", values=(transaction["category"], transaction["amount"], transaction["date"]))

    def update_summary(self):
        total_income = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        total_expenses = sum(t["amount"] for t in self.transactions if t["amount"] < 0)
        balance = total_income + total_expenses
        self.summary_label.config(text=f"Total Income: ${total_income:.2f} | Total Expenses: ${-total_expenses:.2f} | Balance: ${balance:.2f}")

    def clear_inputs(self):
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

    def filter_transactions(self, event):
        selected_category = self.filter_category.get()
        if selected_category == "All":
            self.update_transaction_list()
        else:
            filtered_transactions = [t for t in self.transactions if t["category"] == selected_category]
            self.transaction_list.delete(*self.transaction_list.get_children())
            for transaction in filtered_transactions:
                self.transaction_list.insert("", "end", values=(transaction["category"], transaction["amount"], transaction["date"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
