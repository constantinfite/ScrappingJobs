import pandas as pd
from src.transformers.post_date import transform_post_date
from src.transformers.location import get_departement, get_city


def transform_all(raw_df):
    raw_df["post_date"] = transform_post_date(raw_df["Post Day"])
    raw_df["department"] = get_departement(raw_df["Location"])
    raw_df["city"] = get_city(raw_df["Location"])

    transform_df = raw_df.drop(columns=["Post Day", "Location"])
    transform_df = raw_df[["company_name", "job_title", "city", "department", "post_date", "extracted_date", "job_link"]]

    return transform_df
