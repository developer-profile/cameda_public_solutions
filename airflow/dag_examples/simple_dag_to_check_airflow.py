from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=15),
}

with DAG(
    dag_id="test_dag",
    default_args=default_args,
    description="Простой тестовый DAG для проверки работы Airflow",
    schedule_interval="@daily",
    start_date=datetime(2024, 11, 11),
    catchup=False,
) as dag:

    def print_hello():
        print("Hello from Airflow!")

    hello_task = PythonOperator(task_id="print_hello_task", python_callable=print_hello)

    hello_task
