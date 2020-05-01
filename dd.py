import kafka
from kafka import KafkaProducer
#import KafkaProducer
import time
from random import randint
import json
import random


class KafkaProducerC:

    brokers, topic = "localhost:9092", "prices-topic"
    print("========start=====")
    producer = KafkaProducer(bootstrap_servers=brokers)

    def __init__(self):
        a = 1
        while a == 1:
            self.message_publisher()

    def message_publisher(self):
        print("=========Start producer =========")
        # {"match":123,"price":1.38}
        data = {}
        data['match'] = randint(111, 999)
        data['price'] = round(random.random(), 2)
        json_data = json.dumps(data)
        print("=====Json data type===={}".format(type(json_data)))
        print("=====Json Data ==={}".format(json_data))
        self.producer.send(self.topic, json_data)
        self.producer.flush()
        time.sleep(10)
        print("========Data is sent successfully to kafka topic {}============".format(self.topic))


KafkaProducerC()