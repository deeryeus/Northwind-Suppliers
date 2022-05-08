from flask import Flask
from flask import render_template
from database import get_supplier_info, get_supplier_products, get_categories, get_category_info

app = Flask(__name__)

@app.route("/")
def main():

    company_locations = get_supplier_info()

    return render_template('suppliers.html', company_locations=company_locations)


@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):

    products = get_supplier_products(supplier_id)

    return render_template('products.html', products=products)


@app.route("/categories")
def categories():

    categories = get_categories()

    return render_template('categories.html', categories=categories)

@app.route("/categories/<int:category_id>")
def category_info(category_id):

    category_info = get_category_info(category_id)

    return render_template('category_info.html', category_info=category_info)