from app import app, shopee, models, controller
import time, json
from datetime import datetime, date, timedelta
from flask import request, jsonify, render_template, url_for

@app.route('/')
def index():
	today = datetime.today()
	pass_15 = today - timedelta(days=15)
	create_time_from	= int(time.mktime(pass_15.timetuple()))
	create_time_to		= int(time.mktime(today.timetuple()))

	GetOrdersList	= shopee.GetOrdersList(create_time_from,create_time_to,100)
	data = json.loads(GetOrdersList.text)
	return data

@app.route('/checkpayment/<ordersn>')
def checkpayment(ordersn):
	today = datetime.today()
	pass_15 = today - timedelta(days=15)
	create_time_from	= int(time.mktime(pass_15.timetuple()))
	create_time_to		= int(time.mktime(today.timetuple()))

	CheckPayment	= shopee.GetTransactionList(create_time_from,create_time_to,100)
	data = json.loads(CheckPayment.text)

	return  controller.addPayment(data,ordersn)

@app.route('/addorder/<ordersn>')
def addorder(ordersn):
	ordersn_list = []
	ordersn_list.append(ordersn) 
	GetOrderDetails	= shopee.GetOrderDetails(ordersn_list)
	data = json.loads(GetOrderDetails.text)

	return controller.GetOrder(data)
