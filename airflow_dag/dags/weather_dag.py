from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import task.weather_extraction
# Define default arguments for the DAG
default_args = {
    'owner': 'thinh pham',
    'start_date': datetime(2023, 9, 9),
    'retries': 1,
}


# Instantiate the DAG using the 'with' statement
with DAG(
    'weather_pipeline',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=None,  # Set the schedule interval based on your requirements
    catchup=False,  # If set to True, backfill will be enabled
) as dag:

    # Create the first task using PythonOperator
    task1 = PythonOperator(
        task_id='check_api_available',
        python_callable=task.check_api_request('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=8c34946f386e3da68c6ede01e504113e'),
    )

    # Create the second task using PythonOperator
    # task2 = PythonOperator(
    #     task_id='task_2',
    #     python_callable=task_2,
    # )

    # Set task dependencies
    check_api_available
