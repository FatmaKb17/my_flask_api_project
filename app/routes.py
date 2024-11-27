from flask import Blueprint, jsonify, request, render_template
from .models import ProductModel

main = Blueprint('main', __name__)

# Route pour récupérer tous les produits
@main.route('/products', methods=['GET'])
def get_products():
    products = ProductModel.get_all_products()
    return jsonify(products)

# Route pour ajouter un produit
@main.route('/products', methods=['POST'])
def add_product():
    data = request.json
    response = ProductModel.add_product(data)
    return jsonify(response), 201

# Route pour récupérer un produit spécifique
@main.route('/products/<string:name>', methods=['GET'])
def get_product(name):
    product = ProductModel.get_product_by_name(name)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

# Route pour la page d'accueil
@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
