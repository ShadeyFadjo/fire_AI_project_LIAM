import utils
import polars as pl
from prefect import flow, task

config=utils.get_config()

#@task(name='filter-conf-and-type')
def filter_conf_type(df):
    if 'type' in df.columns:
        df = df.filter((pl.col('confidence') >= 50) & (pl.col('type') == 0))
    else:
        df = df.filter(pl.col('confidence') >= 50)
    return df

#@task
def drop_columns(df):
    return df.drop(['scan','track','satellite','instrument','confidence','version','bright_t31','daynight','type'])

#@task
def cast_acq_date(df):
    return df.with_columns(pl.col("acq_date").str.strptime(pl.Date, "%d/%m/%Y"))

#@task
def write_csv(df,raw_file):
    loc_new_file=config['firms_NASA']['interim_data_location'] + raw_file.split('/')[-1]
    df.write_csv(loc_new_file)
    return loc_new_file

#@flow(name='preprocess-new-data')
def preprocess(raw_file):
    df=pl.read_csv(new_file, separator=';')
    df=filter_conf_type(df)
    df=drop_columns(df)
    df=cast_acq_date(df)
    new_file=write_csv(df,raw_file) 
    print('file processed: '+ new_file + ' created')