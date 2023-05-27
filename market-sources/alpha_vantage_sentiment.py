import os
import json
import pika
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["ALPHA_VANTAGE_API_KEY"]
RABBITMQ_QUEUE = os.environ["RABBITMQ_QUEUE"]
RABBITMQ_EXCHANGE = os.environ["RABBITMQ_EXCHANGE"]


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={API_KEY}"
r = requests.get(url)
data = r.json()
print(data)
channel.basic_publish(exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_QUEUE, body=json.dumps(data))

print(data)
