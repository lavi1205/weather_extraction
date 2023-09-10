from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
import sys
sys.path.append("task")
import weather_extraction
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

    start_pipeline = DummyOperator(
        task_id='START'
    )
    # Create the first task using PythonOperator
    check_api_available = PythonOperator(
        task_id='check_api_available',
        python_callable=weather_extraction.check_api_request,
        op_kwargs={'api_url':'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=8c34946f386e3da68c6ede01e504113e'}
    )
    
    # Create the second task using PythonOperator
    tranform_data = PythonOperator(
        task_id='tranform_data',
        python_callable=weather_extraction.extract_data,
        op_kwargs={'api_url':'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=8c34946f386e3da68c6ede01e504113e'}
    )
    # Move data to S3

    move_data = PythonOperator(
        task_id='move_data',
        python_callable=weather_extraction.move_data_s3,
        op_kwargs={'api_url':'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=8c34946f386e3da68c6ede01e504113e'}
    )

    # Set task dependencies
    start_pipeline >> check_api_available >> tranform_data >> move_data
