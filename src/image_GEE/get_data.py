import utils
from prefect import flow, task
import image_GEE.utils as image_utils
import numpy as np
import geemap
from PIL import Image

config=utils.get_config()

@task
def get_sat_images(initial_date,until_date):
    return image_utils.get_sat_images(initial_date,until_date)

@task
def update_yaml_data_last_date(end_date):
    utils.update_yaml('gee','data_last_date',end_date)

@task
def gee_images_into_png(sat_images,initial_date,until_date):
    start_date=initial_date
    gray_normalization = 253        # 509-256
    firms_country_images=sat_images
    country=image_utils.get_country()

    while start_date < until_date:
        end_date=utils.add_days(start_date)
        print('downloading image; start_date: ' + start_date + ', end_date: '+ end_date)
        filter_mada_fire= firms_country_images.filterDate(start_date, end_date)
        image=filter_mada_fire.max()
        imaget21=image.select('T21')
        arrayt21 = geemap.ee_to_numpy(imaget21, region=country, scale=2000)
        arrayt21 = np.squeeze(arrayt21, axis=2)
        arrayt21[arrayt21 != 0] -= gray_normalization
        arrayt21 = arrayt21.astype(np.uint8)
        img = Image.fromarray(arrayt21, mode='L')
        file_name=start_date + ',' + end_date + '.png'
        dire=config['gee']['raw_data_location']
        directory=dire+file_name
        img.save(directory)
        start_date=utils.add_days(end_date,1)
    update_yaml_data_last_date(end_date)
    
@flow(name='get-new-images')
def get_data(end_date):
    image_utils.gee_authenticate()
    start_date=utils.add_days(config['gee']['data_last_date'],1)
    sat_images=get_sat_images(start_date,end_date)
    gee_images_into_png(sat_images,start_date,end_date)
    print('Get new images is done!')