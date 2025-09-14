from get_user_expense import get_user_expense
from save_expense_to_file import save_expense_to_file
from summarize_expenses import summarize_expenses


def main() -> None:
    BUDGET: float = 2000.00
    EXPENSES_FILE_PATH = "expenses.csv"

    print("Welcome to the expense tracker! 🤑\n")

    expense = get_user_expense()

    save_expense_to_file(expense, EXPENSES_FILE_PATH)

    summarize_expenses(EXPENSES_FILE_PATH, BUDGET)


if __name__ == "__main__":
    main()
