import os
import json

from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv()

BROKERS = os.getenv('BROKERS').split(',')
print(BROKERS)

consumer = KafkaConsumer(
  os.getenv('TOPIC_PROTEINAS'), 
  bootstrap_servers=BROKERS,
  group_id="consumidores")

for message in consumer:
  payload = json.loads(message.value)
  print(payload)