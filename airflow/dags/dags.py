import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator


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
    start = DummyOperator(task_id="Start")

    end = DummyOperator(task_id="End")
