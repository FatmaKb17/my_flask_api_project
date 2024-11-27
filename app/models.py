from . import mongo

class ProductModel:
    """Classe pour interagir avec la collection 'products' dans MongoDB."""

    @staticmethod
    def get_all_products():
        """Récupère tous les produits de la base de données."""
        products = mongo.db.products.find()
        result = []
        for product in products:
            result.append({
                "name": product['name'],
                "price": product['price'],
                "stock": product['stock']
            })
        return result

    @staticmethod
    def add_product(data):
        """Ajoute un nouveau produit à la base de données."""
        mongo.db.products.insert_one({
            "name": data['name'],
            "price": data['price'],
            "stock": data['stock']
        })
        return {"message": "Product added successfully!"}

    @staticmethod
    def get_product_by_name(name):
        """Récupère un produit spécifique par son nom."""
        product = mongo.db.products.find_one({"name": name})
        if product:
            return {
                "name": product['name'],
                "price": product['price'],
                "stock": product['stock']
            }
        return None
