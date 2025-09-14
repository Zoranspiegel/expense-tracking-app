from expense import Expense


def save_expense_to_file(expense: Expense, file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")

    print(
        f"\nYou've added {expense.name} (${expense.amount}) to your expenses of {expense.category} category.\n")
