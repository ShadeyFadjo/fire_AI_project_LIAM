import polars as pl
from prefect import flow, task

#@flow(name='preprocess-new-data')
def preprocess(raw_file):
    new_file = raw_file 
    print('file processed: '+ new_file + ' created')