from confluent_kafka import Consumer, KafkaError
import json

class MyKafkaConsumer:
    def __init__(self) -> None:
        # Consumer configuration
        self.conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'my-group',
            'auto.offset.reset': 'earliest'
        }

        # Create Consumer instance
        self.consumer = Consumer(self.conf)
    
    def receive_message(self):
        # Subscribe to topic
        self.consumer.subscribe(['test-topic'])

        # Process messages
        try:
            while True:
                msg = self.consumer.poll(1.0)
                
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print('Reached end of partition')
                    else:
                        print(f'Error: {msg.error()}')
                else:
                    # Parse the message value
                    try:
                        value = json.loads(msg.value().decode('utf-8'))
                        print(f'Received message: {value}')
                        print(f'Topic: {msg.topic()}, Partition: {msg.partition()}, Offset: {msg.offset()}')
                    except json.JSONDecodeError:
                        print(f'Failed to parse message value: {msg.value()}')

        except KeyboardInterrupt:
            pass
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()

if __name__ == '__main__':
    myConsumer = MyKafkaConsumer()
    myConsumer.receive_message()