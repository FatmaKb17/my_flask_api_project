from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config["MONGO_URI"] = "mongodb://localhost:27017/my_database"
    mongo.init_app(app)

    # Import and register routes
    from .routes import main
    app.register_blueprint(main)

    return app
