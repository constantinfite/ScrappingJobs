import pandas as pd
import numpy

from src.extract.extract import extract_all_pages
from src.transformers.transform import transform_all
from src.load.load import load

if __name__ == '__main__':
    extracted_df = extract_all_pages("data%20engineer", "Bordeaux", "permanent")
    extracted_df.to_csv("jobs.csv", encoding='utf-8')

    transform_df = transform_all(extracted_df)
    transform_df.to_csv("jobs_transform.csv", encoding='utf-8',index=False)
    #transform_df = pd.read_csv('jobs_transform.csv')

    load(transform_df)

    # print(transform_df)
