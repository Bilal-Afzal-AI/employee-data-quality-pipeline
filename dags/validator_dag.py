from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys

# Airflow container ke andar project root path
sys.path.append("/opt/airflow")

from validation_engine.validator import run_validations



default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def run_validator_task():
    print("🔥 Starting Validation DAG")

    metrics = run_validations()

    print("✅ Validation Completed")
    print("Metrics:", metrics)


with DAG(
    dag_id="validator_dag",
    default_args=default_args,
    description="Postgres to Validation to MLflow Pipeline",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["data-quality", "mlflow"],
) as dag:

    run_validation_task = PythonOperator(
        task_id="run_validation",
        python_callable=run_validator_task,
    )