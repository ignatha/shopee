from app import app, shopee
import time, json
from datetime import datetime, date
from flask import request, jsonify, render_template, url_for

@app.route('/')
def index():
	create_time_from	= int(time.mktime(datetime(2020, 3, 1).timetuple()))
	create_time_to		= int(time.mktime(datetime.today().timetuple()))

	GetOrdersList	= shopee.GetOrdersList(create_time_from,create_time_to,100)
	data = json.loads(GetOrdersList.text)
	return data


@app.route('/orderdetail/<ordersn>')
def orderdetail(ordersn):
	ordersn_list = []
	ordersn_list.append(ordersn) 
	GetOrderDetails	= shopee.GetOrderDetails(ordersn_list)
	data = json.loads(GetOrderDetails.text)
	return data

@app.route('/vue')
def vue():
	return render_template('vue.html')