# File: mlflow_tracking/mlflow_utils.py

import mlflow_tracking
from datetime import datetime
from shared.mlflow_tracking.mlflow_utils import log_dq_metrics

# MLflow experiment configuration
EXPERIMENT_NAME = "Employee_Data_Quality"

def init_mlflow():
    """Initialize MLflow experiment"""
    mlflow_tracking.set_tracking_uri("file:///E:/EmployeeDataQuality/mlflow_service/mlruns")  # Local folder for mlflow tracking
    mlflow_tracking.set_experiment(EXPERIMENT_NAME)

def log_dq_metrics(metrics: dict):
    """
    Log data quality metrics to MLflow
    metrics: dict with keys like total_checked, fail_null, fail_email, fail_salary, fail_age, pass_all
    """
    init_mlflow()
    with mlflow_tracking.start_run(run_name=f"DQ_Run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
        for key, value in metrics.items():
            mlflow_tracking.log_metric(key, value)
        mlflow_tracking.log_param("run_time", str(datetime.now()))
        print("✅ Metrics logged to MLflow successfully")

# Example usage for testing independently
if __name__ == "__main__":
    example_metrics = {
        "total_checked": 100,
        "fail_null": 5,
        "fail_email": 2,
        "fail_salary": 1,
        "fail_age": 0,
        "pass_all": 92
    }
    log_dq_metrics(example_metrics)