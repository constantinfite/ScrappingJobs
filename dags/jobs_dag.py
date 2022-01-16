from datetime import timedelta
from airflow import DAG
import datetime
from airflow.operators.python import PythonOperator
from dags import jobs_etl

# Define the default_args dictionary
default_args = {
  'owner': 'fite',
  'start_date': datetime,
  'retries': 2
}

dag = DAG('jobs_dag', default_args=default_args)

run_etl = PythonOperator(
    task_id='whole_job_scraping_etl',
    python_callable=jobs_etl.etl_jobs(),
    dag=dag,
)

run_etl