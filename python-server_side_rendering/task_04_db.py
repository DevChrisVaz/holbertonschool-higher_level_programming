from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/contact')
def contact():
      return render_template('contact.html')

@app.route('/items')
def items():
      with open('items.json', 'r') as f:
        data = json.load(f)
      items_list = data.get("items", [])
      return render_template('items.html', items=items_list)
  
def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        try:
            products = read_json_file('products.json')
        except Exception as e:
            return render_template('product_display.html', error_message="Error reading JSON file.")
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
        except Exception as e:
            return render_template('product_display.html', error_message="Error reading CSV file.")
    elif source == 'sql':
        try:
            products = read_sqlite_database('products.db')
        except Exception as e:
            return render_template('product_display.html', error_message="Error reading SQLite database.")
    else:
        return render_template('product_display.html', error_message="Wrong source specified. Please use 'json', 'csv', or 'sql'.")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
       app.run(debug=True, port=5000)