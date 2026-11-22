import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_db"
)

cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)

# sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
# cursor.execute(sql, ("books", 7, 280))
# conn.commit()
sql = "SELECT * FROM products WHERE name = %s"
cursor.execute(sql, ("eraser",))
print(cursor.fetchone())

cursor.execute(sql, ("xyz",))
print(cursor.fetchone())

cursor.close()
conn.close()