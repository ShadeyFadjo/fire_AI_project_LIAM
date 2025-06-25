import utils
import polars as pl
from prefect import flow, task

config=utils.get_config()

def start_end_date():
    start_date=config['firms_NASA']['data_last_date']
    end_date=utils.add_days(start_date)
    return start_date,end_date

@task
def update_yaml_data_last_date():
    start_date,end_date=start_end_date()
    utils.update_yaml('firms_NASA','data_last_date',end_date)

@task
def pre_save():
    start_date,end_date=start_end_date()
    start_date=utils.add_days(start_date,1)
    file_name='modis_'+start_date+'_'+end_date
    url=config['firms_NASA']['API_url']+start_date
    df=pl.read_csv(url)
    df=df.drop(['country_id'])
    new_file=config['firms_NASA']['raw_data_location']+file_name+'.csv'
    return df,new_file

@flow(name='get-new-data')
def get_data():
    df, new_file=pre_save()
    df.write_csv(new_file, separator=';')
    update_yaml_data_last_date()
    return new_file
    print('file: '+ new_file + ' created')