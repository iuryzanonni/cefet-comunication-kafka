import os
import random
import json

from dotenv import load_dotenv
from kafka import KafkaProducer
from kafka.errors import KafkaError

load_dotenv()

BROKERS = os.getenv('BROKERS').split(',')
TOPIC = os.getenv('TOPIC_PROTEINAS')

def serializer(message):
  return json.dumps(message).encode('utf-8')

payload = {}

producer = KafkaProducer(
  bootstrap_servers=["localhost:9092", "localhost:9093", "localhost:9094"], 
  api_version=(0,11,5),
  value_serializer=serializer)

while True:
  n = random.randint(0, 1000)
  payload["id"] = n
  payload["message"] = str(input())
  try:
    producer.send(TOPIC, value=payload)
  except KafkaError as e:
    print(e)  
    
  print("Send a new message: [0] yes, [1] no")
  opt = int(input())
  if opt == 1:
    break
