from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime, date


class penjualan(db.Model):
    ordersn = db.Column(db.String(20), primary_key=True)
    create_time = db.Column(db.DateTime,  nullable=True,
        default=datetime.utcnow)
    buyer_username = db.Column(db.String(50),  nullable=True)
    order_status = db.Column(db.String(20), nullable=True)
    shipping_carrier = db.Column(db.String(20), nullable=True)
    ship_by_date = db.Column(db.DateTime, nullable=True,
        default=datetime.utcnow)
    tracking_no = db.Column(db.String(20), nullable=True)
    total_amount = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))


class recipient_address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ordersn = db.Column(db.String(20), db.ForeignKey('penjualan.ordersn'),  nullable=True)
	penjualan = db.relationship('penjualan',backref=db.backref('recipient_address', lazy=True))
	city = db.Column(db.String(30),  nullable=True)
	district = db.Column(db.String(30),  nullable=True)
	full_address = db.Column(db.String(1000),  nullable=True)
	name = db.Column(db.String(30),  nullable=True)
	phone = db.Column(db.String(15),  nullable=True)
	state = db.Column(db.String(30),  nullable=True)
	town = db.Column(db.String(30),  nullable=True)
	zipcode = db.Column(db.String(7),  nullable=True)

class order_detail(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ordersn = db.Column(db.String(20), db.ForeignKey('penjualan.ordersn'),  nullable=True)
	penjualan = db.relationship('penjualan',backref=db.backref('order_detail', lazy=True))
	item_id = db.Column(db.String(30),  nullable=True)
	item_name = db.Column(db.String(100),  nullable=True)
	item_sku = db.Column(db.String(10),  nullable=True)
	variation_original_price = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))
	variation_discounted_price = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))
	variation_name = db.Column(db.String(30),  nullable=True)
	variation_id = db.Column(db.String(15),  nullable=True)
	variation_quantity_purchased = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))

class pembelian(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ordersn = db.Column(db.String(20), db.ForeignKey('penjualan.ordersn'),  nullable=True)
	penjualan = db.relationship('penjualan',backref=db.backref('pembelian', lazy=True))
	amount = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))
	status = db.Column(db.String(10),  nullable=True)

class pembayaran(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ordersn = db.Column(db.String(20), db.ForeignKey('penjualan.ordersn'),  nullable=True)
	penjualan = db.relationship('penjualan',backref=db.backref('pembayaran', lazy=True))
	amount = db.Column(db.Numeric(precision=10, asdecimal=False, decimal_return_scale=None))
	status = db.Column(db.String(10),  nullable=True)