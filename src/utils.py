from datetime import datetime, timedelta

def add_days(date_str,dayadd=10):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=dayadd)
    return new_date.strftime("%Y-%m-%d")