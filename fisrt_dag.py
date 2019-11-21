from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {

    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1)

}

dag = DAG('first_dag', default_args=default_args, schedule_interval=timedelta(seconds=3))

t1 = BashOperator(
    task_id='write_date',
    bash_command='/home/robert/work/goUrban/goUrban/bin/python ~/airflow/dags/date_writer.py',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 10',
    retries=3,
    dag=dag)

t1 >> t2