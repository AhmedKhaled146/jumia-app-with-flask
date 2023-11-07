from flask_restful import Resource, marshal_with
from app.models import Product, Category
from app.products.serializer import product_serializer
from app.products.parser import product_request_parser
from app.models import db


class ProductListResource(Resource):
    @marshal_with(product_serializer)
    def get(self):
        products = Product.query.all()
        return products, 200


    @marshal_with(product_serializer)
    def post(self):
        data = product_request_parser.parse_args()
        print(data)
        return product, 201



class ProductResource(Resource):

    @marshal_with(product_serializer)
    def get(self, product_id):
        product = Product.query.get(product_id)

        return product, 200



    @marshal_with(product_serializer)
    def put(self, product_id):
        product = Product.query.get(product_id)
        data = product_request_parser.parse_args()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.image = data['image']
        product.in_stock = data['in_stock']
        db.session.add(product)
        db.session.commit()
        print(product)
        return  product




    def delete(self, product_id):
        product = Product.query.get(product_id)
        db.session.delete(product)
        db.session.commit()
        return "deleted", 204

