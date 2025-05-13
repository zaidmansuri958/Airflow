from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime ,timedelta


def hello_world_py():
    print("hello world from python operator")

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    # 'email_on_failure':False,
    # 'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=5),
}

dag=DAG(
    'dummy_dag',
    default_args=default_args,
    description='A dummy dag',
    schedule_interval=None,
    start_date=datetime(2025, 5, 13),
    catchup=False,
    tags=['dev'],
)


t1=BashOperator(
    task_id='bash_hello',
    bash_command='echo "Hello world from bash operator"',
    dag=dag 
)

t2=PythonOperator(
    task_id="python_hello",
    python_callable=hello_world_py,
    dag=dag
)

t1>>t2