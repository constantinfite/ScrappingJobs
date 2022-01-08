from src.extract.extract import extract_all_pages
from src.transformers.transform import transform_all
# from src.load import

if __name__ == '__main__':
    extracted_df = extract_all_pages()

    transform_df = transform_all(extracted_df)
    print(extracted_df)
# df.to_csv("jobs.csv", encoding='utf-8')
