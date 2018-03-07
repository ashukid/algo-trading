from cryptopia_api import Api
from config import API_KEY, API_SECRET

# creating the wrapper for crytopia api
api_wrapper = Api(API_KEY, API_SECRET)

print("Getting history...")
print(api_wrapper.get_tradehistory('SPT/BTC'))