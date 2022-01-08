import pandas as pd
from src.transformers.post_date import transform_post_date


def transform_all(raw_df):

    raw_df["Post Date"] = transform_post_date(raw_df["Post Date"])

    return raw_df


