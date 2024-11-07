import json
from confluent_kafka import Consumer, KafkaError
from GroqAgent import AgentCreator, agent_monitor_prompt
from MongoDB import DBManager

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

        agentCreator = AgentCreator()
        db_manager = DBManager()

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
                    try:
                        # Parse the message value
                        value = json.loads(msg.value().decode('utf-8'))
                        print(f'Received message: {value}')
                        print(f'Topic: {msg.topic()}, Partition: {msg.partition()}, Offset: {msg.offset()}')

                        # Managing the flow of user input and agents' output
                        user_input = value['prompt']
                        agent_output = agentCreator.create_agent(user_input)
                        agentMonitorPrompt = agent_monitor_prompt(user_input, agent_output)
                        agent_monitor_output = agentCreator.create_agent(agentMonitorPrompt)
                        agent_monitor_output['monitored_agent_id'] = agent_output['agent_id']

                        # Logging the activity of simple agents and agent monitors
                        db_manager.add_agent(agent_output)
                        db_manager.add_agent(agent_monitor_output)
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