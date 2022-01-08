import pandas as pd
from src.transformers.post_date import transform_post_date
from src.transformers.location import get_departement, get_city


def transform_all(raw_df):

    raw_df["Post Date"] = transform_post_date(raw_df["Post Day"])
    raw_df["Departement"] = get_departement(raw_df["Location"])
    raw_df["City"] = get_city(raw_df["Location"])

    transform_df = raw_df.drop(columns=["Post Day", "Location"])

    return transform_df
