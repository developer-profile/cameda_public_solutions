from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import boto3
import botocore
import botocore.config
import yandexcloud


def _upload_file_to_s3(bucket_name: str, object_path: str, content: str):
    sdk = yandexcloud.SDK()

    def provide_cloud_auth_header(request, **kwargs):
        request.headers.add_header("X-YaCloud-SubjectToken", sdk._channels._token_requester.get_token())

    session = boto3.Session()
    session.events.register('request-created.s3.*', provide_cloud_auth_header)
    client = session.resource(
        "s3",
        endpoint_url="https://storage.yandexcloud.net",
        config=botocore.config.Config(
            signature_version=botocore.UNSIGNED,
            retries=dict(
                max_attempts=5,
                mode="standard",
            ),
        ),
    )
    client.Bucket(name=bucket_name).put_object(Key=object_path, Body=content)


def upload_file_to_s3():
    _upload_file_to_s3(
        bucket_name="vlbel-airflow",
        object_path="data/airflow.txt",
        content="Hello from Managed Airflow!"
    )


with DAG(
    dag_id='upload_file_to_s3',
    start_date=datetime(2024, 5, 24),
    schedule="@once",
    catchup=False,
) as dag:
    PythonOperator(
        task_id='upload_file_to_s3',
        python_callable=upload_file_to_s3,
    )
