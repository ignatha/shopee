from app import app, shopee, models
import time, json
from datetime import datetime, date, timedelta

def GetOrder(data):
	for item in data['orders']:
		p = models.penjualan(
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
		r = models.recipient_address(
			city=recipent['city'],
			district=recipent['district'],
			full_address=recipent['full_address'],
			name=recipent['name'],
			phone=recipent['phone'],
			state=recipent['state'],
			town=recipent['town'],
			zipcode=recipent['zipcode']
			)
		
		p.recipient_address.append(r)

		for detail in item['items']:
			o = models.order_detail(
				item_id=detail['item_id'],
				item_name=detail['item_name'],
				item_sku=detail['item_sku'],
				variation_original_price=detail['variation_original_price'],
				variation_discounted_price=detail['variation_discounted_price'],
				variation_name=detail['variation_name'],
				variation_id=detail['variation_id'],
				variation_quantity_purchased=detail['variation_quantity_purchased']
				)
			p.order_detail.append(o)

		models.db.session.add(p)
		models.db.session.commit()