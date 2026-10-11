expenses = []

def add_expense():
    name = input("What is the name of the expense? ")
    amount = float(input("what is the amount of the expense?"))
    category = input("What is the category of the expense? ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added!")
    
def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")
    total = sum(expense['amount'] for expense in expenses)
    print("Total expenses: ", total)

while True:
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
                add_expense()
        elif choice == "2":
                show_expenses()
        elif choice == "3":
                print("Exiting...")
                break
        else:
                print("Invalid choice. Please try again.")