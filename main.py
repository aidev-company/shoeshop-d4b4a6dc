from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

port = int(os.environ.get('PORT', 8080))

# Sample in-memory data store for demonstration purposes
products = [
    {'id': 1, 'name': 'Product 1', 'category': 'Category 1', 'brand': 'Brand 1', 'price': 10.99, 'size': 'L', 'color': 'Red'},
    {'id': 2, 'name': 'Product 2', 'category': 'Category 2', 'brand': 'Brand 2', 'price': 9.99, 'size': 'M', 'color': 'Blue'},
    {'id': 3, 'name': 'Product 3', 'category': 'Category 1', 'brand': 'Brand 3', 'price': 12.99, 'size': 'S', 'color': 'Green'}
]

@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    brand = request.args.get('brand')
    price = request.args.get('price')
    size = request.args.get('size')
    color = request.args.get('color')
    search = request.args.get('search')

    filtered_products = products

    if category:
        filtered_products = [p for p in filtered_products if p['category'] == category]
    if brand:
        filtered_products = [p for p in filtered_products if p['brand'] == brand]
    if price:
        price_range = price.split(',')
        filtered_products = [p for p in filtered_products if float(price_range[0]) <= p['price'] <= float(price_range[1])]
    if size:
        filtered_products = [p for p in filtered_products if p['size'] == size]
    if color:
        filtered_products = [p for p in filtered_products if p['color'] == color]
    if search:
        filtered_products = [p for p in filtered_products if search.lower() in p['name'].lower()]

    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)