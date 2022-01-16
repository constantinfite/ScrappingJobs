import sqlalchemy
import sqlite3

DATABASE_LOCATION = "sqlite:///my_jobs.sqlite"


def load(transform_df):
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_jobs.sqlite')
    cursor = conn.cursor()

    sql_query_create_table = """
        CREATE TABLE IF NOT EXISTS my_jobs(
            company_name VARCHAR(200),
            job_title VARCHAR(200),
            city VARCHAR(200),
            department INT,
            post_date DATE,
            extracted_date DATE,
            job_link,
            
            CONSTRAINT primary_key_constraint PRIMARY KEY (job_link) 
        )
        """
    sql_query_drop_table = """
        DROP TABLE IF EXISTS my_jobs
    """

    #cursor.execute(sql_query_drop_table)

    cursor.execute(sql_query_create_table)

    print("Opened database successfully")

    for i in range(len(transform_df)):
        # If element already exists in the table
        try:
            transform_df.iloc[i:i + 1].to_sql("my_jobs", engine, index=False, if_exists='append')
        except:
            pass

    conn.close()
    print("Close database successfully")
