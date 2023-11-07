from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads' # To upload file

# # Database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# db = SQLAlchemy(app)


# model
class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)


@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)


@app.route('/product/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)

    if request.method == 'POST':
        # first one i get the product details
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        in_stock = bool(request.form.get('in_stock'))
        new_image = request.files['image']
        print(new_image)
        print(product.image)

        if product.image:
            # if images already exist
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], product.image)
            if os.path.exists(file_path):
                # Delete the existing image
                os.remove(file_path)

            # Save new image
            filename = secure_filename(new_image.filename)
            new_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = f'uploads/{filename}'
        else:
            image_path = product.image

        # Update the product details and image path
        product.name = name
        product.description = description
        product.price = price
        product.in_stock = in_stock
        product.image = image_path

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('edit_product.html', product=product)

@app.route('/product/<int:id>/delete')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('home'))



@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        in_stock = bool(request.form.get('in_stock'))
        image = request.files['image']

        # Handle file upload and store the image in the 'static' directory
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = f'uploads/{filename}'
        else:
            image_path = None

        # Create the product and store it in the database
        product = Product(name=name, description=description, price=price, in_stock=in_stock, image=image_path)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('create_product.html', action='Create')




# if __name__ == '__main__':
#     app.run(debug=True)
