import utils
import polars as pl
from prefect import flow, task

config=utils.get_config()

@task(name='filter-conf-and-type')
def filter_conf_type(df):
    if 'type' in df.columns:
        df = df.filter((pl.col('confidence') >= 50) & (pl.col('type') == 0))
    else:
        df = df.filter(pl.col('confidence') >= 50)
    return df

@task
def drop_columns(df):
    df = df.drop(['scan','track','satellite','instrument','confidence','version','bright_t31','daynight'])
    return df

# @task
# def cast_acq_date(df):
#     df=df.with_columns(pl.col("acq_date").str.strptime(pl.Date, "%d/%m/%Y"))
#     return df

@task
def write_csv(df,raw_file):
    loc_new_file=config['firms_NASA']['interim_data_location'] + raw_file.split('/')[-1]
    df.write_csv(loc_new_file,separator=';')
    return loc_new_file

@flow(name='preprocess-new-data-csv')
def preprocess(raw_file):
    new_file = write_csv((drop_columns(filter_conf_type(pl.read_csv(raw_file, separator=';')))), raw_file)
    print('file processed: '+ new_file + ' created')