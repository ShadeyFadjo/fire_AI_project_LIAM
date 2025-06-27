import csv_NASA.get_data as get_data, csv_NASA.preprocessing as preprocessing
from prefect import flow

@flow(name='pipeline-csv')
def pipeline():
    raw_file=get_data.get_data()
    preprocessing.preprocess(raw_file)