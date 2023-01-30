from multiprocessing.connection import Client
import pymongo
import pandas as pd
import numpy as np
import json



client = pymongo.MongoClient("mongodb+srv://bhushan:bhushankiran.1@cluster0.vkpxwnm.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r'E:\Projects\Project-AIWalaBro\insurance.csv')
DATABASE_NAME = 'INSURANCE'
COLLECTION_NAME = 'INSURANCE_PROJECT'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"we are reading rows and columns:{df.shape}")
    
        # reset index and stored in orginal data
    df.reset_index(drop= True, inplace= True)
    
        # converting data into key value pair format
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
        #inserting the transpose data into the database
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    
    