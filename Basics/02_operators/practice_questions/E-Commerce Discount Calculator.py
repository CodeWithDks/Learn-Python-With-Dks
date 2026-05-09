# E-Commerce Discount Calculator
# A customer is shopping online and has a cart total of $150. The e-commerce platform offers a discount based on the following criteria:
# - If the cart total is greater than $100, the customer gets a 10%
# - If the cart total is greater than $200, the customer gets a 20%
# - If the cart total is greater than $300, the customer gets a 30%
# Write a Python program to calculate the final price after applying the appropriate discount based on the cart total.

# Taking user input for cart total.

cart_total = float(input("Enter your cart amount: ")) # 150

if cart_total > 300:
    discount = cart_total * 30 / 100

elif cart_total > 200:
    discount = cart_total * 20 / 100

elif cart_total > 100:
    discount = cart_total * 10 / 100

else:
    discount = 0

final_amount = cart_total - discount

print(f"Discount: {discount}$")
print(f"Final amount: {final_amount}$")