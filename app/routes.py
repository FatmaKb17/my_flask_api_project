from flask import Blueprint, jsonify, request, render_template
from . import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = mongo.db.products.find()
    return render_template('index.html', products=products)

@main.route('/products', methods=['GET'])
def get_products():
    products = mongo.db.products.find()
    result = []
    for product in products:
        result.append({
            "name": product.get('name'),
            "price": product.get('price'),
            "stock": product.get('stock')
        })
    return jsonify(result)

@main.route('/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or not data.get('name') or not data.get('price') or not data.get('stock'):
        return jsonify({"message": "Missing data! Name, price, and stock are required."}), 400
    
    mongo.db.products.insert_one({
        "name": data.get('name'),
        "price": data.get('price'),
        "stock": data.get('stock')
    })
    return jsonify({"message": "Product added successfully!"}), 201
