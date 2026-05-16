import pandas as pd
import psycopg2

from mlflow_utils import log_metrics


# ===================================
# PostgreSQL Connection
# ===================================

def get_connection():

    conn = psycopg2.connect(
        host="dq_postgres",
        port="5432",
        database="airflow_db",
        user="postgres",
        password="Postgres123456"
    )

    return conn


# ===================================
# Main Validation Function
# ===================================

def run_validations():

    print("🔥 Validation Started")

    conn = get_connection()

    query = """
        SELECT
            employee_id,
            first_name,
            last_name,
            email,
            salary
        FROM employees
    """

    df = pd.read_sql(query, conn)

    conn.close()

    print("✅ Data Loaded")

    # ===================================
    # Validation Checks
    # ===================================

    total_records = len(df)

    null_emails = df["email"].isnull().sum()

    duplicate_employee_ids = (
        df["employee_id"]
        .duplicated()
        .sum()
    )

    invalid_salary = (
        df["salary"] <= 0
    ).sum()

    passed_records = total_records - (
        null_emails +
        duplicate_employee_ids +
        invalid_salary
    )

    failed_records = (
        null_emails +
        duplicate_employee_ids +
        invalid_salary
    )

    metrics = {

        "total_records": int(total_records),

        "null_emails": int(null_emails),

        "duplicate_employee_ids": int(duplicate_employee_ids),

        "invalid_salary": int(invalid_salary),

        "passed_records": int(passed_records),

        "failed_records": int(failed_records)
    }

    print(metrics)

    # ===================================
    # MLflow Logging
    # ===================================

    log_metrics(
        run_name="employee_data_quality_run",
        metrics=metrics
    )

    print("✅ Logged To MLflow")

    return metrics