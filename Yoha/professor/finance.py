# personal_finance_agent/agent.py

from rich import print, box
from rich.table import Table
from datetime import datetime
import csv
import os
import openai

openai.api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"  # Replace with your key

CSV_FILE = "database.csv"

# Ensure CSV file exists
def init_db():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "type", "amount", "category"])

def add_transaction(entry_type, amount, category):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().date(), entry_type, amount, category])

def get_summary():
    income = 0
    expense = 0
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row['amount'])
            if row['type'] == 'income':
                income += amt
            elif row['type'] == 'expense':
                expense += amt
    return income, expense, income - expense

def show_summary_table():
    income, expense, savings = get_summary()
    table = Table(title="Daily Finance Summary", box=box.SIMPLE)
    table.add_column("Category", style="cyan")
    table.add_column("Amount (PKR)", justify="right", style="green")
    table.add_row("Income", f"{income:.2f}")
    table.add_row("Expenses", f"{expense:.2f}")
    table.add_row("Savings", f"{savings:.2f}", style="bold yellow")
    print(table)

def ask_financial_tip():
    question = input("\n💬 Ask your finance question (e.g., how to save more?):\n> ")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},
            {"role": "user", "content": question}
        ]
    )
    print("\n🤖 Advice:")
    print(f"[italic cyan]{response.choices[0].message['content']}[/italic cyan]")


def main():
    init_db()
    print("[bold green]💰 Welcome to Personal Finance Planner Agent 💰[/bold green]\n")

    while True:
        print("\n[1] Add Income\n[2] Add Expense\n[3] Show Summary\n[4] Ask for AI Advice\n[5] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Enter amount: "))
            cat = input("Enter category (e.g., Salary): ")
            add_transaction("income", amt, cat)
        elif choice == '2':
            amt = float(input("Enter amount: "))
            cat = input("Enter category (e.g., Food): ")
            add_transaction("expense", amt, cat)
        elif choice == '3':
            show_summary_table()
        elif choice == '4':
            ask_financial_tip()
        elif choice == '5':
            print("[bold red]Exiting. Stay smart with your money![/bold red]")
            break
        else:
            print("[red]Invalid choice![/red]")

if __name__ == '__main__':
    main()
