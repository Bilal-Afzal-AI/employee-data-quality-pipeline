import mlflow

EXPERIMENT_NAME = "employee_data_quality"


def log_metrics(run_name: str, metrics: dict):

    # Airflow container se host machine ke mapped MLflow port ko call karega
    mlflow.set_tracking_uri("http://host.docker.internal:5000")

    mlflow.set_experiment(EXPERIMENT_NAME)

    with mlflow.start_run(run_name=run_name):

        for key, value in metrics.items():
            mlflow.log_metric(key, float(value))

        mlflow.log_param("source", "airflow_dag")

    print("✅ MLflow logged:", metrics)