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

@app.route('/transactionlist')
def transactionlist():
	today = datetime.today()
	pass_15 = today - timedelta(days=15)
	create_time_from	= int(time.mktime(pass_15.timetuple()))
	create_time_to		= int(time.mktime(today.timetuple()))

	TransactionList	= shopee.GetTransactionList(create_time_from,create_time_to,100)
	data = json.loads(TransactionList.text)

	payment_order_list = data["transaction_list"]
	for item in payment_order_list:
		if item['ordersn'] == '':
			payment_order_list.remove(item)

	return  json.dumps(payment_order_list)


@app.route('/orderdetail/<ordersn>')
def orderdetail(ordersn):
	ordersn_list = []
	ordersn_list.append(ordersn) 
	GetOrderDetails	= shopee.GetOrderDetails(ordersn_list)
	data = json.loads(GetOrderDetails.text)
	print data
	controller.GetOrder(data)

	return "ok"

@app.route('/vue')
def vue():
	return render_template('vue.html')