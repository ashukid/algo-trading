from cryptopia_api import Api
from config import API_KEY, API_SECRET
import time

# creating the wrapper for crytopia api
api_wrapper = Api(API_KEY, API_SECRET)

def order(coin_pair,market,desired_coin_pair_price,trade_option,amount):

	print("Getting current balance...")
	current_balance = api_wrapper.get_balance('BTC')
	print("Current Balance : {} bitcoins\n".format(current_balance[0]['Available']))


	while True:
		print("Getting current market status ...")
		coin_stats = api_wrapper.get_market(coin_pair)
		coin_price = coin_stats[0]["LastPrice"]
		coin_price = float(format(coin_price,'.8f'))
		print("Current Exchange rate : {}".format(coin_price))
		print("Desired Exchange rate : {}\n".format(desired_coin_pair_price))

		if(trade_option == 'Buy'):
			if(coin_price > desired_coin_pair_price):
				print("Price is higher than desired\n")
				break
		else:
			if(coin_price < desired_coin_pair_price):
				print("Price is lower than desired\n")
				break

		if(coin_price == desired_coin_pair_price):
			print("Price matched, placing order...")
			order,error = api_wrapper.submit_trade(market,trade_option,desired_coin_pair_price,amount)
			if error is not None:
				print("Error : {}".format(error))
			else:
				print("Success !")
				print("Order Placed with order id : {}\n".format(order['OrderId']))
				print("fetching remaining balance...")
				remaining_balance = api_wrapper.get_balance('BTC')
				print("remaining Balance : {}".format(remaining_balance[0]['Available']))
			break
		time.sleep(0.01)




