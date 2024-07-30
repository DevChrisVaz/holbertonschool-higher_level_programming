from flask import Flask, render_template, request
import json
import csv


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
      
      file_name = "items.json"
      items = read(file_name)
      return render_template('items.html', items=items)

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
    else:
        return render_template('product_display.html', error_message="Wrong source specified. Please use 'json' or 'csv'.")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error_message="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
       app.run(debug=True, port=5000)