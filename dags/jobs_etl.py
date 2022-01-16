from src.extract.extract import extract_all_pages
from src.transformers.transform import transform_all
from src.load.load import load


def etl_jobs():
    extracted_df = extract_all_pages("data%20engineer", "lille", "permanent")
    extracted_df.to_csv("jobs.csv", encoding='utf-8')

    transform_df = transform_all(extracted_df)
    transform_df.to_csv("jobs_transform.csv", encoding='utf-8',index=False)

    load(transform_df)