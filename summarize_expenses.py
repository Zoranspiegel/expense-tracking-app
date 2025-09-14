import datetime
import calendar
from expense import Expense


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
