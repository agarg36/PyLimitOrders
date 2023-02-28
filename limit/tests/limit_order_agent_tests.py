import unittest
from limit_order_agent import LimitOrderAgent
from order import OrderStatus, BuyOrSell

class LimitOrderAgentTest(unittest.TestCase):

    def setUp(self):
	self.limitorderBook = LimitOrderAgent()
	self.limitorderBook.add_order(BuyOrSell.BUY, 'AAPL', 100, 98.45)
	self.limitorderBook.add_order(BuyOrSell.BUY, 'AAPL', 300, 99.45)
	self.limitorderBook.add_order(BuyOrSell.BUY, 'AAPL', 100, 100.45)
	self.limitorderBook.add_order(BuyOrSell.BUY, 'AAPL', 100, 101.45)
	self.limitorderBook.add_order(BuyOrSell.BUY, 'AAPL', 100, 102.45)
	self.limitorderBook.add_order(BuyOrSell.SELL, 'AAPL', 100, 98.45)
	self.limitorderBook.add_order(BuyOrSell.SELL, 'AAPL', 300, 99.45)
	self.limitorderBook.add_order(BuyOrSell.SELL, 'AAPL', 100, 100.45)
	self.limitorderBook.add_order(BuyOrSell.SELL, 'AAPL', 100, 101.45)
	self.limitorderBook.add_order(BuyOrSell.SELL, 'AAPL', 100, 102.45)

    def tearDown(self):
	pass

    def test_add_order(self):
	# Add an order and assert that the length of non-cancelled orders in orderbook increases
	pass

    def test_modify_order(self):
	# Update an order and assert that the length of non-cancelled orders in orderbook remains the same 
	pass

    def test_cancel_order(self):
	# Cancel an order and assert that the length of non-cancelled orders in orderbook decreases by 1
	pass

    def test_submit_order_on_market_event(self):
	# Send a market price of 100 for product-id 'AAPL' and assert that if the buy orders with limit >= 100 are moved to PROCESSED
	# Send a market price of 100 for product-id 'AAPL' and assert that if the sell orders with limit <= 100 are moved to PROCESSED
	pass

    def test_submit_orders_ignores_cancelled_orders(self):
	# Send a market price of 100 and add a delay in the submit_orders method. In the interim, call cancel_order on buy orders having limit price >= 100
        # Assert that the cancelled orders show status as CANCELLED = instead of PROCESSED
	pass
