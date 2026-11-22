from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_db"
)
cursor = conn.cursor(dictionary=True)


def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


def find_product(name):
    sql = "SELECT * FROM products WHERE name = %s LIMIT 1"
    cursor.execute(sql, (name,))
    return cursor.fetchone()

def total_inventory_value():
    cursor.execute("SELECT SUM(price * quantity) AS total FROM products")
    result = cursor.fetchone()
    return result["total"] or 0

@app.route("/")
def home():
    return "Inventory API is running"


@app.route("/products", methods=["GET"])
def list_products():
    products = get_all_products()
    for p in products:
        p["price"] = float(p["price"])
    return jsonify(products)


@app.route("/products/<name>", methods=["GET"])
def get_product(name):
    product = find_product(name)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    product["price"] = float(product["price"])
    return jsonify(product)


@app.route("/total", methods=["GET"])
def total():
    return jsonify({"total": float(total_inventory_value())})

if __name__ == "__main__":
    app.run(debug=True)