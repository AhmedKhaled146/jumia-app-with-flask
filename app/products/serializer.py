from flask_restful import fields

categorySerializer = {
    'id': fields.Integer,
    'name': fields.String,
}

product_serializer={
    'id':fields.Integer,
    'name': fields.String,
    'image': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'in_stock': fields.Boolean,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
    'category_name': fields.Nested(categorySerializer)
}
