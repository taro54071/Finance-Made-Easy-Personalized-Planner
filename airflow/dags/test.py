import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator


args = {"owner": "Taro"}
desc = "Testing"


def check_file():
    import subprocess

    result = subprocess.run(
        ["diff", "/opt/airflow/config/text1.txt", "/opt/airflow/config/text2.txt"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        # files are identical
        pass
    else:
        # files are not identical
        subprocess.run(
            ["cp", "/opt/airflow/config/temp.txt", "/opt/airflow/config/ssf.txt"]
        )


with DAG(
    dag_id="testing",
    default_args=args,
    description=desc,
    start_date=pendulum.datetime(
        year=2023, month=8, day=6, hour=1, minute=47, second=0, tz="Asia/Bangkok"
    ),
    schedule_interval="0 8 * * 1-5",  # Run once on every weekday at 08:00 AM
) as dag:
    check_identical_file = PythonOperator(
        task_id="check_identical_file", python_callable=check_file
    )
