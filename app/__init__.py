from flask import Flask
from app import shopee
from flask_sqlalchemy import SQLAlchemy

# test ini editan

# perubahan di sisi develop

## penmabhaan baru dari develop

app = Flask(__name__)
app.config.from_object('config')

shopee = shopee.shopee(app.config['PARTNER_ID'], app.config['SHOPID'], app.config['KEY'])

db = SQLAlchemy(app)

from app import models, routes

db.create_all()