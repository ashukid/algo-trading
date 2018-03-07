from cryptopia_api import Api
from config import API_KEY, API_SECRET
import main
api_wrapper = Api(API_KEY, API_SECRET)


# predefined variables
coin_name = 'SPT'
how_much_bitcoin = 0.0009000
offset = 0
trade_option = 'Sell'


option = int(raw_input("1. Automatic\n2. Manual\n"))

# manual variables
if(option == 2):
	coin_name = raw_input("The coin name abbreviation (example ETH): ")
	how_much_bitcoin = float(raw_input("Amount of BTC to pay with : "))
	offset = float(input("Offset rate of the coin pair : "))
	trade_option = raw_input("Buy/Sell : ")

# getting coin stats
coin_pair = coin_name+'_BTC'
market = coin_name+'/BTC'
print("Getting current market status...")
coin_pair_stats = api_wrapper.get_market(coin_pair)
coin_pair_price = coin_pair_stats[0]["LastPrice"]
coin_pair_price = float(format(coin_pair_price,'.8f'))
print("Current exchange rate : {}".format(coin_pair_price))
if(trade_option == 'Buy'):
	desired_coin_pair_price = float(format(coin_pair_price + (coin_pair_price*(offset/float(100))),'.8f'))
	print("Desired Exchange rate : {}".format(desired_coin_pair_price))
	amount = round(how_much_bitcoin/desired_coin_pair_price)
	print("Number of coins you can buy : {}".format(amount))
else:
	desired_coin_pair_price = float(format(coin_pair_price - (coin_pair_price*(offset/float(100))),'.8f'))
	print("Desired Exchange rate : {}".format(desired_coin_pair_price))
	amount = round(how_much_bitcoin/desired_coin_pair_price)
	print("Number of coins you can sell : {}".format(amount))



# calling the order function
main.order(coin_pair,market,desired_coin_pair_price,trade_option,amount)

