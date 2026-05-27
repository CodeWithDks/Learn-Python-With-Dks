'''Shopping Cart System

Create empty shopping cart list.

Ask user to:

add items
print cart items
Example
Cart:
Laptop
Mouse
Keyboard
Skills
append()
loops
dynamic data handling'''

# Initialize an empty shopping cart list
shopping_cart = []

while True:
    print("\nShopping Cart System")
    print("1. Add Item")
    print("2. Print Cart Items")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_cart.append(item)
        print(f'Item "{item}" added to the cart.')
        
    elif choice == '2':
        if shopping_cart:
            print("Your Shopping Cart:")
            for idx, item in enumerate(shopping_cart, start=1):
                print(f"{idx}. {item}")
        else:
            print("Your shopping cart is empty.")
            
    elif choice == '3':
        print("Exiting the Shopping Cart System. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        