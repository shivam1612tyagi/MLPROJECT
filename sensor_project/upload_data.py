import pandas as pd
import json
from src.logger import logging

#unifrom resource indentifier 
uri = "mongodb+srv://shivam1612tyagi:<password>cluster0.u0vl4ba.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name 
DATABASE_NAME="ML_Project"
COLLECTION_NAME="Wafer_Fault"

#read data as an dataframe
df=pd.read_csv("notebooks/data/wafer_23012020_041211.csv")
#df=df.drop("Unamed: 0",axis=1)

#convert tha data into JSON
json_record = list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

logging.info("Data is uploaded to MongoDB")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
