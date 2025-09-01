from expense import Expense


def main() -> None:
    EXPENSES_FILE_PATH = "expenses.csv"

    print("Welcome to the expense tracker! 🤑\n")

    expense = get_user_expense()

    save_expense_to_file(expense, EXPENSES_FILE_PATH)
    
    summarize_expenses(EXPENSES_FILE_PATH)


def get_user_expense() -> Expense:
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount ($): "))

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎮 Fun",
        "✨ Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        category_number = input(f"Enter a category number {value_range}: ")

        value_options = ""
        for number in range(1, len(expense_categories) + 1):
            value_options += str(number)

        if len(category_number) == 1 and category_number in value_options:
            expense_category = expense_categories[int(category_number) - 1]
            new_expense = Expense(name=expense_name,
                                  category=expense_category, amount=expense_amount)

            return new_expense
        else:
            print("🔴 Invalid option. Please try again!\n")


def save_expense_to_file(expense: Expense, file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

    print(
        f"\nYou've added {expense.name} (${expense.amount}) to your expenses of {expense.category} category.\n")


def summarize_expenses(file_path: str):
    print(f"Summarizing user expenses from {file_path} file...")


if __name__ == "__main__":
    main()
