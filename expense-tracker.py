import datetime
import calendar
from expense import Expense


def main() -> None:
    BUDGET: float = 2000.00
    EXPENSES_FILE_PATH = "expenses.csv"

    print("Welcome to the expense tracker! 🤑\n")

    expense = get_user_expense()

    save_expense_to_file(expense, EXPENSES_FILE_PATH)

    summarize_expenses(EXPENSES_FILE_PATH, BUDGET)


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
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")

    print(
        f"\nYou've added {expense.name} (${expense.amount}) to your expenses of {expense.category} category.\n")


def summarize_expenses(file_path: str, budget: float):
    expenses: list[Expense] = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")

            line_expense = Expense(
                name=expense_name,
                category=expense_category,
                amount=float(expense_amount)
            )

            expenses.append(line_expense)

    amount_by_category: dict[str, float] = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"\n💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent

    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]    
    remainint_days = days_in_month - now.day
    daily_budget = remaining_budget / remainint_days
    print(green(f"👉 Budget Per Day: ${daily_budget}"))

def green(text: str):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()
