import os
from dotenv import load_dotenv

from binance.spot import Spot

load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

client = Spot()
print(client.time())

client = Spot(key=api_key, secret=secret_key)

print(client.account())

