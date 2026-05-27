# Railway Ticket Booking System
# A railway ticket booking system allows users to book tickets for train journeys. The system should have the following features:


'''Railway Ticket Booking System

Take:

age
gender
ticket price

Rules:

children under 5 → free
senior citizens → 30% discount
females → 10% discount
others → full price

Calculate final payable amount.

Skills Combined
conditions
arithmetic
real-world logic
business rules
'''

age = int(input("Enter your age: "))
gender = input("Enter your gender (m/f): ").lower()
ticket_price = float(input("Enter ticket price: "))

if age < 5:
    print("Free travel")

elif age >= 60:
    discount = ticket_price * 30 / 100
    print("Your ticket price is:", ticket_price - discount)

elif gender == "f":
    discount = ticket_price * 10 / 100
    print("Your ticket price is:", ticket_price - discount)

else:
    print("Full price:", ticket_price)