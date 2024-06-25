transactions = []
budgets = {}


def add_transaction(transaction_type, amount, category, description):
    transactions.append(
        {
            "transaction": transaction_type,
            "amount": amount,
            "category": category,
            "description": description,
        }
    )
    with open("data.txt", "a") as file:
        file.write(f"{transaction_type},{amount},{category},{description}\n")


def view_transaction():
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            keys = line.strip().split(",")
            print(f"{index + 1}: {keys[0]} | {keys[1]} | {keys[2]} | {keys[3]}")


def delete_transaction(index):
    with open("data.txt", "r") as file:
        lines = file.readlines()
        zero_based_index = index - 1
    if 0 <= zero_based_index < len(lines):
        del lines[zero_based_index]
        with open("data.txt", "w") as file:
            file.writelines(lines)


def set_budgets(category, amount):
    budgets[category] = amount
    with open("budgets.txt", "w") as file:
        for c, a in budgets.items():
            file.write(f"{c},{a}\n")


def view_budgets():
    with open("budgets.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            category, amount = line.strip().split(",")
            print(f"{category}: {amount}")


def generate_report():
    report = {}
    total_expenses = 0.0
    total_income = 0.0
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                transaction_type, amount, category, description = line.strip().split(
                    ","
                )
                amount = float(amount)
                if transaction_type == "income":
                    total_income += amount
                elif transaction_type == "expense":
                    if category not in report:
                        report[category] = 0
                    report[category] += amount
                    total_expenses += amount
        print("Spending Report:")
        for category, total in report.items():
            print(f"{category}: {total:.2f}")
        print(f"Total Expenses: {total_expenses:.2f}")
        print(f"Total Income: {total_income:.2f}")
        print(f"Remaining Balance: {total_income-total_expenses:.2f}")
    except FileNotFoundError:
        print("No transactions found. Creating a new data file.")
        open("data.txt", "w").close()


def display_menu():
    print("\nPersonal Finance Manager")
    print("1. Add Income/Expense")
    print("2. View Transactions")
    print("3. Delete Transaction")
    print("4. Set Budget")
    print("5. View Budget")
    print("6. Generate Report")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            transaction_type = input("Income or Expense: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            add_transaction(transaction_type, amount, category, description)
        elif choice == "2":
            view_transaction()
        elif choice == "3":
            index = int(input("Enter the index of the transaction to delete: "))
            delete_transaction(index)
        elif choice == "4":
            category = input("Category: ")
            amount = float(input("Amount: "))
            set_budgets(category, amount)
        elif choice == "5":
            view_budgets()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice")
            print("Please choose a number between 1 and 7")


if __name__ == "__main__":
    main()
