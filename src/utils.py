from datetime import datetime, timedelta
import yaml

config_file='config.yaml'

def add_days(date_str,dayadd=10):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=dayadd)
    return new_date.strftime("%Y-%m-%d")

def get_config():
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f) 
    return config

def update_yaml(grp_str,params_str,new_str):
    config=get_config()
    config[grp_str][params_str] = new_str
    with open(config_file, "w") as file:
        yaml.safe_dump(config, file, default_flow_style=False,sort_keys=False)