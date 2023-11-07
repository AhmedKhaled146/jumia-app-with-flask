import os
from flask import Flask
from app.config import project_config as App_Config
from app.models import db
from app.products.views import *
from app.products import product_blueprint
from app.category import category_blueprint
from flask_migrate import Migrate
from flask_restful import Api
from app.products.api_views import ProductListResource, ProductResource

def create_app(config_name='prd'):
    app = Flask(__name__)
    Current_App_Config = App_Config[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = Current_App_Config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(Current_App_Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.add_resource(ProductListResource, '/api/products')
    api.add_resource(ProductResource, '/api/products/<int:product_id>')



    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html')

    app.register_blueprint(product_blueprint)
    app.register_blueprint(category_blueprint)

    app.debug = True
    return app
