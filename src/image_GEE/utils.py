import ee
import utils

config=utils.get_config()

def gee_authenticate():
    ee.Authenticate()
    ee.Initialize(project=config['gee']['project_name'])

def get_country(country='Madagascar'):
    pays = ee.FeatureCollection("FAO/GAUL/2015/level0")
    firenena = pays.filter(ee.Filter.eq('ADM0_NAME', country))
    return firenena

def clip_to_country(img):
  return img.clip(get_country())

def get_sat_images(start_date,end_date):
   firms_image = ee.ImageCollection("FIRMS").filterDate(start_date,end_date)
   firms_images_country = firms_image.map(clip_to_country)
   return firms_images_country