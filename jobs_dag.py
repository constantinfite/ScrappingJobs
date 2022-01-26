from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from jobs_etl import jobs_etl

# Define the default_args dictionary
default_args = {

    'owner': 'fite',
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('jobs_dag', default_args=default_args,
          start_date=datetime(2022, 1, 16),
          schedule_interval="15 * * * *")


def just_a_function():
    print("hello")


run_etl = PythonOperator(
    task_id='whole_job_scraping_etl',
    python_callable=jobs_etl,
    dag=dag,
)

run_etl
