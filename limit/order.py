from enum import Enum

class OrderStatus(Enum):
	NEW=1
	REPLACED=2
	CANCELLED=3
	PROCESSED=4

class BuyOrSell(Enum):
	BUY=1
	SELL=2

Class Order:

	order_id=0

	def __new__(cls):
		order_id += 1	

	def __init__(self,buy_or_sell, product_id, quantity, limit_price):
		self.id = order_id	
		self.buy_or_sell- buy_or_sell		
		self.product_id = product_id
		self.quantity = quantity	
		self.limit_price = limit_price
		self.status = NEW
