from flask import Flask, request, jsonify, render_template, url_for
import shopee, time, json
from datetime import datetime, date

app = Flask(__name__)
app.config.from_object('config')

shopee = shopee.shopee(app.config['PARTNER_ID'], app.config['SHOPID'], app.config['KEY'])

@app.route('/')
def index():
	create_time_from	= int(time.mktime(datetime(2020, 3, 1).timetuple()))
	create_time_to		= int(time.mktime(datetime.today().timetuple()))

	GetOrdersList	= shopee.GetOrdersList(create_time_from,create_time_to,10)
	data = json.loads(GetOrdersList.text)
	return data