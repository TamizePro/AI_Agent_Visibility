import json
from confluent_kafka import Producer

class MyKafkaProducer:
    def __init__(self) -> None:
        # Initialize producer
        self.conf = {'bootstrap.servers': 'localhost:9092'}
        self.producer = Producer(self.conf)
    
    def __delivery_report(self,err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
    
    def send_message(self):
        # Produce message
        for i in range(100):
            data = {'i': 'value'+ str(i)}
            self.producer.produce(
                'test-topic',
                key='key1',
                value=json.dumps(data),
                callback=self.__delivery_report
            )

        # Wait for messages to be delivered
        self.producer.flush()

if __name__ == '__main__':
    myProducer = MyKafkaProducer()
    myProducer.send_message()