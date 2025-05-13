from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago 

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'retries':1,
    'retry_delay':timedelta(minutes=5)
}

dag=DAG(
    'parallel_job_dag',
    default_args=default_args,
    description='parallel dag',
    schedule_interval=timedelta(minutes=2),
    start_date=datetime(2025, 5, 13),
    catchup=False,
    tags=['dev']
)

start_task=BashOperator(
    task_id='start_task',
    bash_command='echo "start task"',
    dag=dag
)

parallel_task_1=BashOperator(task_id='parallel_1',bash_command='echo "parallel taks 1"',dag=dag)
parallel_task_2=BashOperator(task_id='parallel_2',bash_command='echo "parallel taks 2"',dag=dag)
parallel_task_3=BashOperator(task_id='parallel_3',bash_command='echo "parallel taks 3"',dag=dag)

end_task=BashOperator(task_id='end_task',bash_command='echo "end task"',dag=dag)

start_task>>[parallel_task_1,parallel_task_2,parallel_task_3]>>end_task