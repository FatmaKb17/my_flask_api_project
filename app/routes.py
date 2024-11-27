from flask import Blueprint, jsonify, request
from . import mongo

main = Blueprint('main', __name__)

@main.route('/products', methods=['GET'])
def get_products():
    products = mongo.db.products.find()
    result = []
    for product in products:
        result.append({"name": product['name'], "price": product['price'], "stock": product['stock']})
    return jsonify(result)

@main.route('/products', methods=['POST'])
def add_product():
    data = request.json
    mongo.db.products.insert_one({
        "name": data['name'],
        "price": data['price'],
        "stock": data['stock']
    })
    return jsonify({"message": "Product added successfully!"}), 201
