from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Category(db.Model):
    __tablename__='category'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    products= db.relationship('Product', backref='category_name',lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_objects(cls):
        return  cls.query.all()

    @classmethod
    def save_category(cls, request_data):
        category  =cls(**request_data)
        db.session.add(category)
        db.session.commit()
        return category

    @classmethod
    def delete_category(cls,category):
        db.session.delete(category)
        db.session.commit()

    @classmethod
    def edit_category(cls, id, request_form):
        category = cls.query.get(id)
        category.name = request_form.get('name')
        db.session.commit()
        return category



# model
class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    category=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=True,)

