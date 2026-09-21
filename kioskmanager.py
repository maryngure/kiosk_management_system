print('=' * 40)
print('       KIOSK MANAGEMENT SYSTEM')
print('=' * 40)


owner_name = input('What is the kiosk owner name: ').strip().title()
kiosk_name = input('What is the kiosk name: ').strip().title()

print()
print(f'Welcome to {kiosk_name} Kiosk Manager, run by {owner_name}')
print('-' * 40)
print()


import os 


stock = {
    "Milk": {"price": 70, "quantity": 20},
    "Bread": {"price": 65, "quantity": 15},
    "Sugar": {"price": 150, "quantity": 25},
    "Cooking Oil": {"price": 250, "quantity": 12},
    "Rice": {"price": 180, "quantity": 30},
    "Wheat Flour": {"price": 75, "quantity": 18},
    "Tea Leaves": {"price": 120, "quantity": 10},
    "Soda": {"price": 70, "quantity": 24},
    "Biscuits": {"price": 50, "quantity": 35},
    "Eggs": {"price": 20, "quantity": 40}
}

def load_inventory():
    if not os.path.exists("inventory.txt"):
        return None

    stock = {}

    with open("inventory.txt", "r") as file:
        for line in file:
            product, price, quantity = line.strip().split(",")

            stock[product] = {
                "price": int(price),
                "quantity": int(quantity)
            }

    return stock


loaded_stock = load_inventory()

if loaded_stock is not None:
    stock = loaded_stock



def view_stock():
    print()
    print('===== STOCK =====')
    print(f"{'Product':<15}{'Price':>10}{'Quantity':>10}")
    print("-" * 40)

    for product, details in stock.items():
        print(f"{product:<15}{details['price']:>10}{details['quantity']:>10}")

def restock_product():
    print()
    product = input("Enter product name: ").strip().title()

    if product in stock:
        quantity = input("Enter quantity to add: ")

        if quantity.isdigit():
            quantity = int(quantity)
            stock[product]["quantity"] += quantity
            print(f"{product} restocked successfully.")
            print(f"New quantity: {stock[product]['quantity']}")
            print()
        else:
            print("Please enter a valid quantity.")

    else:
        print(f"{product} is not currently in stock.")

        price = input("Enter price: ")
        quantity = input("Enter quantity: ")

        if price.isdigit() and quantity.isdigit():
            price = int(price)
            quantity = int(quantity)

            stock[product] = {
                "price": price,
                "quantity": quantity
            }

            print(f"{product} added successfully.")
            print()
        else:
            print("Please enter valid numbers for price and quantity.")


sales_log = []
sold_products = set()


def sell_product():
    print()
    product = input('Enter product name: ').strip().title()

    if product not in stock:
        print('Product not found')
        return
    
    quantity = input('Enter quantity to sell: ')

    if not quantity.isdigit():
        print('Enter a valid quantity number')
        return
    
    quantity = int(quantity)

    if quantity > stock[product]['quantity']:
        print(f'Not enough stock. Only {stock[product]['quantity']} units available')
        return

    total = quantity * stock[product]['price'] 
    stock[product]['quantity'] -= quantity

    sale = (product, quantity, total)
    sales_log.append(sale)
    sold_products.add(product)

    print('Sale successful!')
    print(f'Product: {product}')
    print(f'Quantity: {quantity}')
    print(f'Total: Ksh {total}')
    print()

def sales_report():
    print()
    print('\n===== SALES REPORT =====')

    if len(sales_log) == 0:
        print('No sales have been recorded')
        return

    total_revenue = 0
    product_quantities = {}

    print(f'{'Product':<15} {'Quantity':>10} {'Total':>10}')
    print('-' * 40)

    for sale in sales_log:
        product, quantity, total = sale

        print(f"{product:<15}{quantity:>10}{total:>10}")

        total_revenue += total

        if product in product_quantities:
            product_quantities[product] += quantity
        else:
            product_quantities[product] = quantity

    best_selling_product = max(product_quantities, key=product_quantities.get)

    print("-" * 40)
    print(f"{'TOTAL REVENUE':<25}Ksh {total_revenue}")
    print(f"Unique products sold: {len(sold_products)}")
    print(f"Best-selling product: {best_selling_product}")
    print(f"Quantity sold: {product_quantities[best_selling_product]}")
    print()

def search_products():
    print()
    search_term = input('Enter product name to search: ').lower()

    found = False

    for product, details in stock.items():
        if search_term in product.lower():
            print(f"{product:<15} Ksh {details['price']:>5}  Quantity: {details['quantity']}")
            found = True

    if not found:
        print('No matches found.')


def save_inventory():
    with open("inventory.txt", "w") as file:
        for product, details in stock.items():
            file.write(f"{product},{details['price']},{details['quantity']}\n")


def save_sales():
    with open("sales.txt", "a") as file:
        for sale in sales_log:
            product, quantity, total = sale
            file.write(f"{product},{quantity},{total}\n")


correct_pin = '3434'
while True:
    pin = input('Input your pin: ')

    if pin == correct_pin:
        print('Pin Accepted. Welcome!')
        print()
        break
    else:
        print('Invalid Pin. Try again.')



while True:
    print()
    print('===== MAIN MENU =====')
    print('1. View Stock')
    print('2. Add/Restock a product')
    print('3. Sell a product')
    print('4. View Sales Report')
    print('5. Search Products')
    print('6. Exit')
    print()

    choice = input('Enter your choice (1-6): ')
    print()

    if not choice.isdigit():
        print('Please enter a number from 1-6: ')
        continue

    choice = int(choice)

    if choice == 1:
        view_stock()
        
    elif choice == 2:
        restock_product()
        
    elif choice == 3:
        sell_product()
        
    elif choice == 4:
        sales_report()

    elif choice == 5:
        search_products()

    elif choice == 6:
        save_inventory()
        save_sales()
        print("Inventory and sales saved.")
        print("Goodbye!")
        break
        

    else:
        print("Invalid choice. Please choose between 1 and 6.")









