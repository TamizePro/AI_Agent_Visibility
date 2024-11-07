import json
from confluent_kafka import Producer
from PromptGenerator import PromptGenerator

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
        promptGenerator = PromptGenerator()

        for i in range(10):
            data = {'prompt': promptGenerator.generate_prompt()}
            self.producer.produce(
                'test-topic',
                key='key',
                value=json.dumps(data),
                callback=self.__delivery_report
            )

        # Wait for messages to be delivered
        self.producer.flush()

if __name__ == '__main__':
    myProducer = MyKafkaProducer()
    myProducer.send_message()