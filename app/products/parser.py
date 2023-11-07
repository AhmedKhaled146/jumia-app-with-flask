from flask_restful import reqparse
import werkzeug


product_request_parser = reqparse.RequestParser()
product_request_parser.add_argument('name', type=str)
product_request_parser.add_argument('image', type=str)
product_request_parser.add_argument('description', type=str)
product_request_parser.add_argument('price', type=float)
product_request_parser.add_argument('in_stock', type=bool)
product_request_parser.add_argument('category_name', type=int)

