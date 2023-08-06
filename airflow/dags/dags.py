import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from asyncio import taskgroups


args = {"owner": "Taro"}
desc = "Pulling daily nav from every rmf and ssf under SCB every weekday at 08:00 AM"

with DAG(
    dag_id="daily_NaV",
    default_args=args,
    description=desc,
    start_date=pendulum.datetime(
        year=2023, month=8, day=6, hour=1, minute=47, second=0, tz="Asia/Bangkok"
    ),
    schedule_interval="0 8 * * 1-5",  # Run once on every weekday at 08:00 AM
) as dag:
@task_group()
def scb():
    import requests
    @task()
    def update_new_fund():
        """
            This task work as a update to ssf_list.txt in config folder.
            Might be optimizable(?), e.g., comparing two txt file by binary trait(?)
        """
