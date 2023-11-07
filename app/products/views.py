from app.products import product_blueprint
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.models import Product, Category
from app.models import db
from flask import current_app
from flask import send_from_directory
import os


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@product_blueprint.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)


@product_blueprint.route('/hello', endpoint='hello')
def sayhello():
    return render_template('page_not_found.html')



@product_blueprint.route('/', endpoint='home')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)


@product_blueprint.route('/<int:id>')
def product(id):
    product = Product.query.get(id)

    if product:
        category = Category.query.get(product.category)
        return render_template('product.html', product=product, category=category)
    else:
        flash("Product not found", "error")
        return redirect(url_for('products.home'))


@product_blueprint.route('/<int:id>/delete', endpoint='delete_product')
def delete_product(id):
    product = Product.query.get(id)

    if product:
        db.session.delete(product)
        db.session.commit()

    return redirect(url_for('products.home'))



@product_blueprint.route('/create', methods=['GET', 'POST'], endpoint='create_product')
def create_product():
    categories = Category.query.all()
    if request.method == "POST":
        image = request.files["image"]
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        else:
            # Handle the case when no image is provided (you can customize this part)
            flash("Image is required to create a product.", "error")
            return render_template('create_product.html', action='Create')

        categoryId = request.form["categoryId"]
        category = Category.query.get(categoryId)

        newProduct = Product(
            name=request.form["name"],
            image=filename,
            description=request.form["description"],
            price=request.form["price"],
            in_stock=request.form.get("in_stock") == "yes",
            category=category.id,
        )
        db.session.add(newProduct)
        db.session.commit()
        return redirect(url_for("products.home"))
    return render_template('create_product.html', action='Create', categories=categories)



@product_blueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)
    categories = Category.query.all()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        in_stock = bool(request.form.get('in_stock'))
        new_image = request.files['image']

        if new_image and allowed_file(new_image.filename):
            filename = secure_filename(new_image.filename)
            new_image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            image_path = f'uploads/{filename}'
        else:
            image_path = product.image

        product.name = name
        product.description = description
        product.price = price
        product.in_stock = in_stock
        product.image = image_path

        db.session.commit()

        return redirect(url_for('products.home'))
    return render_template('edit_product.html', product=product)



@product_blueprint.route('/about', endpoint='about')
def about():
    return render_template('about.html')



@product_blueprint.route('/contact', endpoint='contact')
def contact():
    return render_template('contact.html')
