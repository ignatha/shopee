"""controller.py is file for handle any function in this app
"""
import time, json
from app import app, shopee, models
from datetime import datetime, date, timedelta

def GetOrder(data):
	"""GetOrder function can grab order detail from shopee api and add to the database
	
	Args:
	    data ( json ): response from shopee open platform GetOrderDetails method
	
	Returns:
	    json: msg status 
	"""
	for item in data['orders']:
		order = models.penjualan(
			ordersn=item['ordersn'],
			create_time=datetime.utcfromtimestamp(item['create_time']),
			buyer_username=item['buyer_username'],
			order_status=item['order_status'],
			shipping_carrier=item['shipping_carrier'],
			ship_by_date=datetime.utcfromtimestamp(item['ship_by_date']),
			tracking_no=item['tracking_no'],
			total_amount=item['total_amount']
			)

		recipent = item['recipient_address']
		order_recipent = models.recipient_address(
			city=recipent['city'],
			district=recipent['district'],
			full_address=recipent['full_address'],
			name=recipent['name'],
			phone=recipent['phone'],
			state=recipent['state'],
			town=recipent['town'],
			zipcode=recipent['zipcode']
			)
		
		order.recipient_address.append(order_recipent)

		for detail in item['items']:
			order_detail = models.order_detail(
				item_id=detail['item_id'],
				item_name=detail['item_name'],
				item_sku=detail['item_sku'],
				variation_original_price=detail['variation_original_price'],
				variation_discounted_price=detail['variation_discounted_price'],
				variation_name=detail['variation_name'],
				variation_id=detail['variation_id'],
				variation_quantity_purchased=detail['variation_quantity_purchased']
				)
			order.order_detail.append(order_detail)

		models.db.session.add(order)
		models.db.session.commit()

		response = {
				"status":"success",
				"msg":"Data added successfully"
				}
		return json.dumps(response)

def addPayment(data,ordersn):
	"""addPayment, this method can check if order has been paid
	
	Args:
	    data (json): response from shopee open platform GetTransactionList method
	    ordersn (string): ordersn is identity from shopee order 
	
	Returns:
	    json: msg status
	"""
	payment_order = data["transaction_list"]
	for item in payment_order:
		if item['ordersn'] == ordersn:
			order = models.db.session.query(models.penjualan).get(ordersn)
			payment = models.pembayaran(
				amount=item['amount'],
				status=item['status']
				)
			order.pembayaran.append(payment)
			models.db.session.add(order)
			models.db.session.commit()

			response = {
				"status":"success",
				"msg":"Data updated successfully"
				}
			return json.dumps(response)

	response = {
		"status":"error",
		"msg":"Data not found"
		}
	return json.dumps(response)	