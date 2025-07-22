def main():
    expenses = {}

    print("Welcome to Expense Calculator!")

    while True:
        category = input("Enter expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break

        try:
            amount = float(input(f"Enter amount for '{category}': "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue  

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print(f"Current total for {category}: {expenses[category]}")

    print("\nExpense Summary:")
    total = 0.0
    for cat in expenses:
        print(f"{cat}: {expenses[cat]}")
        total += expenses[cat]

    print(f"\nTotal expenses: {total}")

    for cat in expenses:
        if expenses[cat] == 0:
            continue
    
    print("Thank you for using the Expense Calculator!")

if __name__=="__main__":
    main()