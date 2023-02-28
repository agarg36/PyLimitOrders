from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener
from collections import col
import itertools
from order import Order
import threading
import asyncio
import logging

class LimitOrderAgent(PriceListener):

    orderBook = col.defaultdict(lambda: None)
	
    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()
	self.execution_client = execution_client

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
		
	t=threading.Thread(target=self.send_orders, args=(product_id, price))
	t.start()

    def add_order(self,buy_or_sell, product_id, quantity, limit_price):
        # Add Order  
	order = Order(buy_or_sell, product_id, quantity, limit_price)	
	orderBook[order.id]=order

    def modify_order(self,order_id, quantity, limit_price):
        # Add Order  
	order = orderBook[order.id]
	if order != None:
		order.quantity = quantity
		order.limit_price = limit_price 
		order.status = OrderStatus.REPLACED

    def cancel_order(self,order_id):
        # Add Order  
	order = Order(buy_or_sell, product_id, quantity, limit_price)	
	order = orderBook[order.id]
	if order != None:
		order.status = CANCELLED

    def get_open_orders(self, product_id, market_price):
	for id, order in orderBook.items: 
		if (order.status != OrderStatus.CANCELLED or order.status != OrderStatus.PROCESSED) and order.product_id==product_id and (
			 (order.buy_or_sell==BuyOrSell.SELL and order.limit_price <= market_price ) OR   
			 (order.buy_or_sell==BuyOrSell.BUY and order.limit_price >= market_price) 
		):
			yield id

    def send_orders(self, product_id, market_price):
	asyncio.run(self.submit_orders(product_id, market_price))	


    def submit_orders(self, product_id, market_price):
	for order_id in get_open_orders(product_id, market_price): 
		order = orderBook[order_id]	
		if order != None and (order.status != OrderStatus.CANCELLED or order.status != OrderStatus.PROCESSED):
			try:
				if order.buy_or_sell == BuyOrSell.BUY:
					self.execution_client.buy(order.product_id, order.quantity)
				else:
					self.execution_client.sell(order.product_id, order.quantity)
			except Exception as e:
				logging.exception(e)
			finally:
				order.status = OrderStatus.PROCESSED
