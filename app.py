from flask import Flask
from flask import render_template
from database import get_name_city_country

app = Flask(__name__)

@app.route("/")
def main():

    company_locations = get_name_city_country()

    return render_template('main.html', company_locations=company_locations)