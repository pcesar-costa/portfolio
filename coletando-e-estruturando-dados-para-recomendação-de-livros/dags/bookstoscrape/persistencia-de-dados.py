import os
import json
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

def db_conn():
    load_dotenv()
    mongo_url = os.getenv("MONGO_URI")
    mongo_db = str(os.getenv("MONGO_DB"))

    mongo_client = MongoClient(mongo_url)
    return mongo_client[mongo_db]

def main():
    file_path = Path(f'{Path(__file__).parent}/data/db-import.csv')
    if os.path.isfile(file_path):
        db_import_df = pd.read_csv(file_path, sep=';')
        if not db_import_df.empty:
            db_insert = db_import_df.to_dict(orient='records')

            mongo_db = db_conn()
            mongo_db.books.insert_many(db_insert)

if __name__ == '__main__':
    main()