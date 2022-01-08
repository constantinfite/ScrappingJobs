def transform_extract_date(df_extracted):
    df_extracted["Post Date"] = df_extracted["Post Date"].str.extract('(\d+)')