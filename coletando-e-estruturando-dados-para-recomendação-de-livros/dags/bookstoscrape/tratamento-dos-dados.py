import os
import re
import glob
import pandas as pd

from pathlib import Path
from datetime import datetime as dt
from sklearn.pipeline import Pipeline

files_in_folder = glob.glob(f'./data/pending-*.csv')
pending_files = [f for f in files_in_folder]

data = pd.DataFrame()
for file in pending_files:
    pending_df = pd.read_csv(file, sep=';')
    data = data.append(pending_df)
data.reset_index(drop=True, inplace=True)

def drop_na():
    drop_na = data[data.isna().any(axis=1)].copy()
    data.dropna(inplace=True)
    
def set_price_to_number():
    data['price'] = data['price'].apply(lambda x: x[1:])
    
def set_qty_stock(l):
    try:
        stock = re.search('\((\d+) available\)', l)
        qty_stock = stock[1]
    except:
        qty_stock = 0
    return int(qty_stock)

def set_vars_stock():
    data['qty_in_stock'] = data['in_stock'].apply(set_qty_stock)
    data['in_stock'] = data['qty_in_stock'].apply(lambda x: True if x > 0 else False)
    
def drop_duplicates():
    data.drop_duplicates(inplace=True)
    
def simplify_urls():
    data['url'] = data['url'].apply(lambda x: x.replace('http://books.toscrape.com/catalogue', ''))

cols_order = ['url', 'title', 'category', 'stars', 'price', 'in_stock']
cols_equals = [i for i, j in zip(data.columns.values, data.columns.values) if i == j]

if (not data.empty) and len(cols_equals) == len(cols_order):
    pipe = Pipeline([
        ('drop_na', drop_na()), 
        ('set_price_to_number', set_price_to_number()),
        ('set_vars_stock', set_vars_stock()),
        ('drop_duplicates', drop_duplicates()),
        ('simplify_urls', simplify_urls())
    ])

    data = pipe.fit_transform(data)
    
    for file in pending_files:
        file_rename = file.replace('pending', 'bkp')
        os.rename(file, file_rename)
        
    file_name = Path(f'./data/db-import.csv')
    data.to_csv(file_name, index=False, sep=';')