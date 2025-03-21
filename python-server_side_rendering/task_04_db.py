from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    """Read product data from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading products.json: {e}")
        return []

def read_csv_data():
    """Read product data from CSV file."""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert ID to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        print(f"Error reading products.csv: {e}")
        return []

def read_sql_data():
    """Read product data from SQLite database."""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        
        # Convert SQLite rows to dictionaries
        products = []
        for row in cursor.fetchall():
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        
        conn.close()
        return products
    except Exception as e:
        print(f"Error reading from SQLite database: {e}")
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Load data based on source
    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    elif source == 'sql':
        data = read_sql_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_data = [product for product in data if product['id'] == product_id]
            if not filtered_data:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=filtered_data)
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")
    
    return render_template('product_display.html', products=data)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
