from csv_NASA import get_data as get_data_csv, preprocessing as preprocessing_csv
from image_GEE import get_data as get_data_image

if __name__ == "__main__":
    # csv_NASA
    # new_file = get_data_csv.get_data()
    new_file='../data/raw/csv_NASA/modis/instrument_modis_2025/modis_2025-01-01_2025-04-15'
    preprocessing_csv.preprocess(new_file)

    # gee
    # end_date='2025-06-20'
    # get_data_image.get_data(end_date)