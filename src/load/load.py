import sqlalchemy
import sqlite3

DATABASE_LOCATION = "sqlite:///my_jobs.sqlite"

def load(transform_df):
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_jobs.sqlite')
    cursor = conn.cursor()


    sql_query = """
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

    #cursor.execute("DROP TABLE IF EXISTS my_jobs")
    cursor.execute(sql_query)

    print("Opened database successfully")

    # try:
    transform_df.to_sql("my_jobs", engine, index=False, if_exists='replace')
    # except:
    #     print("Data already exists in the database")

    conn.close()
    print("Close database successfully")
