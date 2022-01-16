from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from jobs_etl import jobs_etl


# Define the default_args dictionary
default_args = {
    'start_date': datetime(2022, 1, 16),
    'owner': 'fite',
    'retries': 2
}

dag = DAG('jobs_dag', default_args=default_args)


def just_a_function():
    print("hello")


run_etl = PythonOperator(
    task_id='whole_job_scraping_etl',
    python_callable=jobs_etl,
    dag=dag,
)

run_etl
