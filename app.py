from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import render_template
from flask_mysqldb import MySQL
from markupsafe import escape


app = Flask(__name__,  static_url_path='',
                    static_folder='static', template_folder='templates')
                    
# local
# application.config['MYSQL_HOST'] = 'localhost'
# application.config['MYSQL_USER'] = 'root'
# application.config['MYSQL_PASSWORD'] = 'Uv1ndu2006'
# application.config['MYSQL_DB'] = 'home_delivary'

# production
# application.config['MYSQL_HOST'] = 'database-1.c5qdsuoy5mft.ap-south-1.rds.amazonaws.com'
# application.config['MYSQL_USER'] = 'admin'
# application.config['MYSQL_PASSWORD'] = ''
# application.config['MYSQL_DB'] = 'home_delivary'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/shopping-cart')
def cart():
    return render_template('shopping-cart.html')

@app.route('/shop')
def cart():
    return render_template('shop.html')
