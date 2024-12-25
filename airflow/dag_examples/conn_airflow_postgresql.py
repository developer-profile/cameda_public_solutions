from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
  dag_id='postgresql_test',
  start_date=datetime(2024, 12, 25),
  schedule="@once",
  catchup=False,
) as dag:
  check_conn = PostgresOperator(
      task_id="check_conn",
      postgres_conn_id='pg',
      sql="SELECT 1;",
  )
