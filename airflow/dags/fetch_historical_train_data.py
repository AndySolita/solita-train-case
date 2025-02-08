from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
from google.cloud import bigquery
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

DAG_VERSION = 1
BASE_URL= f'https://rata.digitraffic.fi/api/v1/trains/'



def get_daily_train_trips(start_date, end_date):
    
    """    Returns a dataframe with daily train trips"""

    # Fetch data between start and end date
    
    delta = timedelta(days=1)
    list_of_daily_results = []

    while start_date <= end_date:
        
        departure_date = start_date.strftime("%Y-%m-%d")

        response = requests.get(url = BASE_URL + departure_date)
        response.raise_for_status() 
    
        list_of_daily_results.append(response.json())
    
        start_date += delta

    logging.info("Created list with daily train trips")

    # Flatten list of results
    
    flat_list = [x for xs in list_of_daily_results for x in xs]
    
    return pd.DataFrame(flat_list)
    


def transform_data():
    pass

    
def load_dataframe_to_bigquery_table(df):
    
    # Initialize BigQuery client
    client = bigquery.Client() # PROJECT_ID inferred from environment
    
    # Define the table reference
    dataset_id = 'ingestion_project'
    table_id = 'daily_train_data'
    table_ref = client.dataset(dataset_id).table(table_id)

    # Load the dataframe into BigQuery
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  
    )

    # Load the DataFrame into BigQuery
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

    # Wait for the job to complete
    job.result()    
    
    logging.info("load_dataframe_to_bigquery_table done")


def main():
    
    daily_train_trips = get_daily_train_trips()
    load_dataframe_to_bigquery_table(daily_train_trips)
    

with DAG(
     dag_id=f"daily_train_data{DAG_VERSION}",
     start_date=datetime(2025, 2, 8),
     schedule_interval="@once",
) as dag:
    
    task = PythonOperator(
        task_id='fetch_daily_train_data',
        python_callable=main,
    )