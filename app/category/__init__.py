from flask import  Blueprint

category_blueprint = Blueprint("category", __name__, url_prefix='/category')

from  app.category import views
