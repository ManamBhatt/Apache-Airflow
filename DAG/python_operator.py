from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args= {
'owner': 'mnm'
'retries': 5,
'retry_delay': timedelta(minutes=5) 
}

def greet():
  print("Hello World!")

with DAG(
  default_args=default_args,
  dag_id='out_dag_with_python',
  start_date=datetime(2024, 04, 06)
  schedule_interval='@daily'
) as dag:

  task1=PythonOperator(
    task_id='greet'
    python_callable=greet
  )

  task1
