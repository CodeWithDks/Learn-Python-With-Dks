'''Build a simple contact book. 
Store at least 4 contacts, 
each with name, phone, and email in a nested dictionary. 
Let the user search for a contact by name and display their details. 
If not found, print "Contact not found". 
Also let the user add a new contact.'''

# create contacts
contacts = {
    'Radha' : {
        'phone' : 952537494,
        'email' : 'radha@gmail.com'
    },
    'Ram' : {
        'phone' : 887383783,
        'email' : 'ram@gmail.com'
    },
    "Krishna": {
        "phone": "96XXXXXXXX",
        "email": "krishna@gmail.com"
    },

    "Sita": {
        "phone": "95XXXXXXXX",
        "email": "sita@gmail.com"
    }
}

print(contacts)

try:

    new_name = input("Enter new contact name: ").title()
    new_phone = input("Enter phone: ")
    new_email = input("Enter email: ")
    contacts[new_name] = {'phone': new_phone, 'email': new_email}
    print(f"{new_name} added successfully.")
    username = input('Enter the username: ').title()

    if username in contacts:
        print(contacts[username])
    else:
        print('Contact not found')
except Exception as e:
    print('Error',e)


'''You have a list of tuples, each containing a product name and its price:
pythonproducts = [("Laptop", 75000), ("Phone", 25000), ("Tablet", 30000), ("Earbuds", 3000), ("Charger", 1500)]
Print all products sorted by price (low to high). 
Then print only products under ₹30,000. 
Then ask the user for a budget and print the most expensive product they can afford.'''

# Products with price
products = [
    ("Laptop", 75000),
    ("Phone", 25000),
    ("Tablet", 30000),
    ("Earbuds", 3000),
    ("Charger", 1500)
]

# 1. Print all products sorted by price (low to high)
print("Products sorted by price:\n")

sorted_products = sorted(products, key=lambda product: product[1])

for name, price in sorted_products:
    print(f"{name}: ₹{price}")

# 2. Print only products under ₹30,000
print("\nProducts under ₹30,000:\n")

for name, price in sorted_products:
    if price < 30000:
        print(f"{name}: ₹{price}")

# 3. Ask the user for a budget
budget = int(input("\nEnter your budget: ₹"))

# 4. Find the most expensive product within the budget
affordable_products = []

for product in products:
    if product[1] <= budget:
        affordable_products.append(product)

if affordable_products:
    best_product = max(affordable_products, key=lambda product: product[1])
    print("\nBest product you can afford:")
    print(f"{best_product[0]}: ₹{best_product[1]}")
else:
    print("\nNo product is available within your budget.")