from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="youtube_iceberg_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_namespace = BashOperator(
        task_id="create_namespace",
        bash_command="""
        docker exec spark-iceberg \
        spark-submit /home/iceberg/jobs/create_namespace.py
        """
    )

    create_table = BashOperator(
        task_id="create_table",
        bash_command="""
        docker exec spark-iceberg \
        spark-submit /home/iceberg/jobs/create_table.py
        """
    )

    load_and_insert = BashOperator(
        task_id="load_and_insert",
        bash_command="""
        docker exec spark-iceberg \
        spark-submit /home/iceberg/jobs/load_and_insert.py
        """
    )

    create_namespace >> create_table >> load_and_insert
