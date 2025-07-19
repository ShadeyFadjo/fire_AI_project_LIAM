from csv_NASA import get_data as get_data_csv, preprocessing as preprocessing_csv, pipeline as csv_pipeline
from image_GEE import get_data as get_data_image

if __name__ == "__main__":
    # csv_NASA

    # raw_file = get_data_csv.get_data()

    # raw_file='../data/raw/csv_NASA/modis/instrument_modis_2025/modis_2025-06-05_2025-06-14.csv'
    # preprocessing_csv.preprocess(raw_file)

    # csv_pipeline.pipeline()

    # gee
    end_date='2025-07-15'
    get_data_image.get_data(end_date)