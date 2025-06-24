import utils
from prefect import flow, task

config=utils.get_config()

# @task
def update_yaml_data_last_date(end_date):
    utils.update_yaml('gee','data_last_date',end_date)

#@flow(name='get-new-data-png')
def get_data():
    print('Get new images is done!')