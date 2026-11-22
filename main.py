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

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_db"
)
cursor = conn.cursor(dictionary=True)

def add_product(name, price, quantity):
    sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, price, quantity))
    conn.commit()

def find_product(name):
    sql = "SELECT * FROM products WHERE name = %s LIMIT 1"
    cursor.execute(sql, (name,))
    return cursor.fetchone()

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def total_inventory_value():
    cursor.execute("SELECT SUM(price * quantity) AS total FROM products")
    result = cursor.fetchone()
    return result["total"] or 0

#
# def total_inventory_value(products):
#     total=0
#     for p in products:
#         total = total + (p['price']* p['quantity'])
#     return total
#
# def add_product(products, name, price, quantity):
#     product = {"name": name, "price": price, "quantity": quantity}
#     products.append(product)
#     return product
#
# add_product(products, "ruler", 15, 40)
# print(len(products))
#
# def find_product(products,name):
#     for p in products:
#         if p["name"] == name:
#             return p
#     return None
#
# found = find_product(products,"bag")
# print(found)
# print(find_product(products,"xyz"))
#
# while True:
#     print("\n1: Add product")
#     print("2: Show All")
#     print("3: Total Value")
#     print("4: Exit")
#     print("5: Search Product")
#     choice = input("Choose: ")
#     if choice == "1":
#         name = input("name: ")
#         price = int(input("price: "))
#         quantity = int(input("quantity: "))
#         add = add_product(products,name,price,quantity)
#         print(add)
#     elif choice == "2":
#         for p in products:
#             print(f"{p['name']},{check_stock(p['quantity'])}")
#     elif choice == "3":
#         print(f"Total value: {total_inventory_value(products)}")
#     elif choice == "4":
#         print("Goodbye")
#         break
#     elif choice == "5":
#         name = input("Name to find: ")
#         found = find_product(products, name)
#         if found is None:
#             print("Not found")
#         else:
#             print(f"Name: {found['name']}")
#             print(f"Price: {found['price']}")
#             print(f"Quantity: {found['quantity']}")
#             print(f"Status: {check_stock(found['quantity'])}")
#     else:
#         print("Invalid choice")

while True:
    print("\n1: Add product")
    print("2: Show All")
    print("3: Total Value")
    print("4: Exit")
    print("5: Search Product")
    print("6: Update quantity")
    print("7: Delete product")
    choice = input("Choose: ")
    if choice == "1":
        name = input("name: ")
        price = int(input("price: "))
        quantity = int(input("quantity: "))
        add = add_product(name, price, quantity)
        print(add)
    elif choice == "2":
        for p in get_all_products():
            print(f"{p['name']}, {p['price']}, {p['quantity']}, {check_stock(p['quantity'])}")
    elif choice == "3":
        print(f"Total value: {total_inventory_value()}")
    elif choice == "4":
        print("Goodbye")
        cursor.close()
        conn.close()
        break
    elif choice == "5":
        name = input("Name to find: ")
        found = find_product(name)
        if found is None:
            print("Not found")
        else:
            print(f"Name: {found['name']}")
            print(f"Price: {found['price']}")
            print(f"Quantity: {found['quantity']}")
            print(f"Status: {check_stock(found['quantity'])}")
    elif choice == "6":
        name = input("Name to find: ")
        found = find_product(name)
        if found is None:
            print("Not found")
        else:
            print(f"Current: {found['name']}, price {found['price']}, quantity {found['quantity']}")
            quantity = int(input('New Quantity: '))
            sql = "UPDATE products SET quantity = %s WHERE name = %s"
            cursor.execute(sql, (quantity,name))
            conn.commit()
            print("Updated")
            print(f"Updated: {found['name']}, price {found['price']},quantity {quantity}")
    elif choice == "7":
        name = input("Name to delete: ")
        found = find_product(name)
        if found is None:
            print("Not found")
        else:
            sql = "DELETE FROM products WHERE name = %s"
            cursor.execute(sql, (name,))
            conn.commit()
            print("Deleted.")
    else:
        print("Invalid choice")
