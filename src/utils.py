from datetime import datetime, timedelta
import yaml

def add_days(date_str,dayadd=10):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=dayadd)
    return new_date.strftime("%Y-%m-%d")

def get_config(config_file='config.yaml'):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f) 
    return config