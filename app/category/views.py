from flask import render_template, request, url_for, redirect
from app.category import category_blueprint
from app.models import  Category

@category_blueprint.route('/list_category', endpoint='list_category')
def index():
    categories  = Category.get_all_objects()
    return render_template('list_category.html', categories= categories)



@category_blueprint.route('/create_category', endpoint='create_category',methods = ['GET', 'POST'])
def create():
    if request.method=='POST':
        category = Category.save_category(request.form)
        return redirect(url_for('category.list_category'))

    return render_template('create_category.html')



@category_blueprint.route("/<int:id>", endpoint="detail")
def category_detail(id):
    currentCategory = Category.query.get(id)
    return render_template("category_detail.html", currentCategory=currentCategory)



@category_blueprint.route("/<int:id>/delete", endpoint="delete")
def deleteCategory(id):
    currentCategory = Category.query.get(id)
    Category.delete_category(currentCategory)
    return redirect(url_for("category.list_category"))
