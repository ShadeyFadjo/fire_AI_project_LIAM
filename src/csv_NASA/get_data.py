import utils
import polars as pl

config=utils.get_config()

def get_data(start_date=config['firms_NASA']['data_last_date']):
    #update config
    #alana le MDG
    start_date=utils.add_days(start_date,1)
    end_date=utils.add_days(start_date)
    file_name='modis_'+start_date+'_'+end_date
    url=config['firms_NASA']['API_url']+start_date
    df=pl.read_csv(url)
    new_file=config['firms_NASA']['raw_data_location']+file_name+'.csv'
    df.write_csv(new_file)
    print('file: '+ new_file + ' created')