"""shopee.py is file for connect this app with shopee open platform
"""
import requests, hmac, hashlib, json, time
from datetime import datetime, date


class shopee:
	"""shopee open platform by Prabowo Ignatha
	
	Attributes:
	    key (string): Key string from Shopee open platform
	    partner_id (int): Partner id from shopee open platform
	    shopid (int): Shop id from your shopee store Authorized in Shopee open platform
	    timestamp (int): unix timestamp integer
	    uri (str): Shopee open platform endpoint
	"""
	uri 		= "https://partner.shopeemobile.com/api/v1/"
	timestamp	= int(time.time())

	def __init__(self, partner_id, shopid, key):
		"""initialization
		
		Args:
		    partner_id (int): Partner id from shopee open platform
		    shopid (int): Shop id from your shopee store Authorized in Shopee open platform
		    key (string): Key string from Shopee open platform
		"""
		self.partner_id 	= partner_id
		self.shopid 		= shopid
		self.key 			= key

	def GetOrdersList(self,create_time_from,create_time_to,pagination_entries_per_page):
		"""method use for handle Shopee open platform GetOrderList
		
		Args:
		    create_time_from (int): Datetime integer
		    create_time_to (int): Datetime integer
		    pagination_entries_per_page (int): Show per page
		
		Returns:
		    requests: response from requests
		"""
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
		"""method use for handle Shopee open platform GetOrderDetails
		
		Args:
		    ordersn_list (list): ordersn list for bulk search
		
		Returns:
		    requests: response from requests
		"""
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


	def GetTransactionList(self,create_time_from,create_time_to,pagination_entries_per_page):
		"""method use for handle Shopee open platform GetTransactionList
		
		Args:
		    create_time_from (int): Datetime Integer
		    create_time_to (int): Datetime Integer
		    pagination_entries_per_page (int): show per page
		
		Returns:
		    requests: response from requests
		"""
		api 		= self.uri+"wallet/transaction/list"
		data		= {
			'partner_id': self.partner_id,
			'shopid' : self.shopid,
			'timestamp' : self.timestamp,
			'create_time_from' : create_time_from,
			'create_time_to' : create_time_to,
			'pagination_entries_per_page' : pagination_entries_per_page,
			'pagination_offset' : 0
			}
		data_string = json.dumps(data,sort_keys=False)
		auth 		= self.Authentication(api,data_string)

		api_request = requests.post(api, data = data_string, headers = {"Content-Type": "application/json", "Authorization": auth}, verify=True)

		return api_request


	def Authentication(self,api,data_string):
		"""method use for Hash Authentication request
		
		Args:
		    api (string): full url end point Shopee open platform
		    data_string (json): Json body for requests
		
		Returns:
		    requests: response from requests
		"""
		string_msg 	= '{}|{}'.format(api,data_string)
		auth 		= hmac.new(
						str(self.key),
						msg=string_msg,
						digestmod=hashlib.sha256
						).hexdigest().upper()

		return auth




