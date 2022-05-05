from flask import Flask
from flask import render_template
from database import get_name_city_country, get_supplier_products, get_supplier

app = Flask(__name__)

@app.route("/")
def main():

    company_locations = get_name_city_country()

    return render_template('suppliers.html', company_locations=company_locations)


@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):

    products = get_supplier_products(supplier_id)

    supplier = get_supplier(supplier_id)

    return render_template('products.html', products=products, supplier=supplier)