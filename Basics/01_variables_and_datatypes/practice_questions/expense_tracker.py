# Challenge 1 — Personal Expense Tracker

# Taking user inputs.
user_name = input("plearse enter your name: ")
monthly_income = float(input("please enter your monthly income: "))
food_expense = float(input("please enter your monthly food expense: "))
rent_expense = float(input("please enter your monthly rent expense: "))
travel_expense = float(input("please enter your monthly travel expense: "))
other_expense = float(input("please enter your monthly other expense: "))


# Calculating total expenses and remaining balance.
total_expense = food_expense + rent_expense + travel_expense + other_expense
remaining_balance = monthly_income - total_expense



# Displaying the results.
print(f"/\n{user_name}, here is your monthly expense report:")
print(f"Total Income: ${monthly_income}")   
print(f"Total Expenses: ${total_expense:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")


                     

