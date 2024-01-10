from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

default_args = {
        'owner' : 'airflow',
        'start_date' : datetime(2022, 11, 12),
}

with DAG(dag_id='example_dag',
        default_args=default_args,
        schedule_interval='@once',
        catchup=False
) as dag:
    start = DummyOperator(task_id = 'start', dag = dag)

    python_operator_example = PythonOperator(
        task_id='python_operator_example',
        python_callable = lambda: print("Hello world! This is an Example Python Operator.")
        )

    end = DummyOperator(task_id = 'end', dag = dag)

    start >> python_operator_example >> end