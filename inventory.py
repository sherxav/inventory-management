def check_stock(quantity):
    if quantity == 0:
        return "OUT OF STOCK"
    elif quantity < 5:
        return "LOW STOCK"
    else:
        return "IN STOCK"

def apply_discount(total):
    if total >1000:
        return (total * 0.9)
    else:
        return (total)

products = [
    {"name": "pen", "price": 10, "quantity": 100},
    {"name": "notebook", "price": 60, "quantity": 4},
    {"name": "bag", "price": 800, "quantity": 0},
    {"name": "calculator", "price": 450, "quantity": 5},
]

def total_inventory_value(products):
    total=0
    for p in products:
        total = total + (p['price']* p['quantity'])
    return total

def add_product(products, name, price, quantity):
    product = {"name": name, "price": price, "quantity": quantity}
    products.append(product)
    return product

def find_product(products,name):
    for p in products:
        if p["name"] == name:
            return p
    return None

while True:
    print("\n1: Add product")
    print("2: Show All")
    print("3: Total Value")
    print("4: Exit")
    print("5: Find Product")
    choice = input("Choose: ")
    if choice == "1":
        name = input("name: ")
        price = int(input("price: "))
        quantity = int(input("quantity: "))
        add = add_product(products,name,price,quantity)
        print(add)
    elif choice == "2":
        for p in products:
            print(f"{p['name']},{check_stock(p['quantity'])}")
    elif choice == "3":
        print(f"Total value: {total_inventory_value(products)}")
    elif choice == "4":
        print("Goodbye")
        break
    elif choice == "5":
        name = input("Name to find: ")
        found = find_product(products,name)
        if found is None:
            print("Not found")
        else:
            print(f"Name: {found['name']}")
            print(f"Price: {found['price']}")
            print(f"Quantity: {found['quantity']}")
            print(f"Status: {check_stock(found['quantity'])}")
    else:
        print("Invalid choice")



