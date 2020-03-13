from flask import Flask
from app import shopee
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

shopee = shopee.shopee(app.config['PARTNER_ID'], app.config['SHOPID'], app.config['KEY'])

db = SQLAlchemy(app)

from app import models, routes

db.create_all()