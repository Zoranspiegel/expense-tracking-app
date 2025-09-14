from expense import Expense


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
