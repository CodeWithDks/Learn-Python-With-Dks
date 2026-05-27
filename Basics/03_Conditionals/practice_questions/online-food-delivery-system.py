# Online food delivery system

'''Online Food Delivery System

Take:

order amount
user membership (yes/no)

Rules:

premium members get free delivery
normal users get free delivery only if order ≥ 500
otherwise ₹40 delivery charge
Skills
nested conditions
logical thinking
business rules'''

# Taking user inputs
order_amount = int(input("Enter your order amount: "))
membership = input("Have membership? (yes/no): ").lower()

if membership == "yes":
    print("Free delivery")

elif membership == "no":
    if order_amount >= 500:
        print("Congratulations! Free delivery.")
    else:
        print("Delivery charge: ₹40")
        print("Final amount:", order_amount + 40)

else:
    print("Invalid input")