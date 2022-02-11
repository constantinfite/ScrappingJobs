import pandas as pd
import numpy
from src import constants

from src.extract.extract import extract_all_pages
from src.transformers.transform import transform_all
from src.load.load import load

df = pd.read_csv("jobs.csv")


def jobs_etl():
    extracted_df = extract_all_pages(constants.JOB_TITLE, constants.LOCATION, constants.DURATION)
    extracted_df.to_csv("jobs.csv", encoding='utf-8')

    transform_df = transform_all(extracted_df)
    transform_df.to_csv("jobs_transform.csv", encoding='utf-8', index=False)

    load(transform_df)

    # print(transform_df)


jobs_etl()


