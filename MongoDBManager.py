from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tamizepro:Tamicrosoft1@cluster0.q8uwm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    print('Here are the available databases: \n')
    dbs = client.list_database_names()
    print(dbs)

    print('Here are the available collections in Agent_Deployer database: \n')
    db = client.get_database('Agent_Deployer')
    col = db.list_collection_names()
    print(col)
except Exception as e:
    print(e)