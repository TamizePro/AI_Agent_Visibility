from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class DBManager:
    def __init__(self) -> None:
        self.uri = "mongodb+srv://tamizepro:Tamicrosoft1@cluster0.q8uwm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.database = self.client.get_database('Agent_Deployer')

    def add_agent(self, agent):
        collection = 'Agent_Monitors' if 'monitored_agent_id' in agent else 'Simple_Agents'
        collection = self.database.get_collection(collection)
        collection.insert_one(agent)

if __name__ == '__main__':
    try:
        db_manager = DBManager()

        db_manager.client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        db_manager.add_agent({
            'agent_id' : 0,
            'agent_input' : "prompt",
            'output' : "output",
            'functions': None,
            'Tools': None,
            "timestamp": None
        })
    except Exception as e:
        print(e)