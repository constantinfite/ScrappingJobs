import pandas as pd
from extracted_date import transform_extract_date


def transform_all(raw_df):
    df_transform__extract_date = transform_extract_date()
    return df_transform__extract_date


