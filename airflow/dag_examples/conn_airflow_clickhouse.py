from airflow.decorators import dag, task
from airflow_clickhouse_plugin.hooks.clickhouse import ClickHouseHook

@dag(schedule=None)
def clickhouse():
    @task
    def query_clickhouse():
        ch_hook = ClickHouseHook(clickhouse_conn_id="ch1")
        result = ch_hook.execute('SELECT * FROM db1.users;')
        print(f'query result: {result}')

    query_clickhouse()

clickhouse()
