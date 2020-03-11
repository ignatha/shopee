import requests, hmac, hashlib, json, time
from datetime import datetime, date


class shopee:
	'shopee_open_platform_prabowo_ignatha'
	uri 		= "https://partner.shopeemobile.com/api/v1/"
	timestamp	= int(time.time())

	def __init__(self, partner_id, shopid, key):
		self.partner_id 	= partner_id
		self.shopid 		= shopid
		self.key 			= key

	def GetOrdersList(self,create_time_from,create_time_to,pagination_entries_per_page):
		api 		= self.uri+"orders/basics"
		data		= {
			'partner_id': self.partner_id,
			'shopid' : self.shopid,
			'timestamp' : self.timestamp,
			'create_time_from' : create_time_from,
			'create_time_to' : create_time_to,
			'pagination_entries_per_page' : pagination_entries_per_page
			}
		data_string = json.dumps(data,sort_keys=False)
		auth 		= self.Authentication(api,data_string)

		api_request = requests.post(api, data = data_string, headers = {"Content-Type": "application/json", "Authorization": auth}, verify=True)

		return api_request

	def GetOrderDetails(self,ordersn_list):
		api 		= self.uri+"orders/detail"
		data		= {
			'partner_id': self.partner_id,
			'shopid' : self.shopid,
			'timestamp' : self.timestamp,
			'ordersn_list' : ordersn_list,
			}
		data_string = json.dumps(data,sort_keys=False)
		auth 		= self.Authentication(api,data_string)

		api_request = requests.post(api, data = data_string, headers = {"Content-Type": "application/json", "Authorization": auth}, verify=True)

		return api_request


	def Authentication(self,api,data_string):
		string_msg 	= '{}|{}'.format(api,data_string)
		auth 		= hmac.new(
						str(self.key),
						msg=string_msg,
						digestmod=hashlib.sha256
						).hexdigest().upper()

		return auth




