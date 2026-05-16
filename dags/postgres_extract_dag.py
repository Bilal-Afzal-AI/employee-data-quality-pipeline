from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

import psycopg2


# =========================================================
# Fetch Employee Data
# =========================================================

def fetch_employee_data():

    print("🔥 Starting PostgreSQL Extraction")

    try:

        # -------------------------------------------------
        # PostgreSQL Connection
        # -------------------------------------------------

        conn = psycopg2.connect(
            host="dq_postgres",
            port="5432",
            database="airflow_db",
            user="postgres",
            password="Postgres123456"
        )

        cursor = conn.cursor()

        print("✅ PostgreSQL Connected")

        # -------------------------------------------------
        # Query
        # -------------------------------------------------

        cursor.execute("""
            SELECT
                employee_id,
                first_name,
                last_name,
                email,
                salary
            FROM employees
        """)

        rows = cursor.fetchall()

        print("\n✅ Employee Data:\n")

        for row in rows:
            print(row)

        print(f"\n✅ Total Records Fetched: {len(rows)}")

        cursor.close()
        conn.close()

        print("✅ Connection Closed")

    except Exception as e:

        print("❌ PostgreSQL Extraction Failed")
        print(str(e))

        raise


# =========================================================
# DAG Definition
# =========================================================

with DAG(

    dag_id="postgres_extract_dag",

    description="PostgreSQL Employee Extraction Pipeline",

    start_date=datetime(2026, 1, 1),

    schedule_interval="@daily",

    catchup=False,

    tags=["postgres", "etl", "employee"],

) as dag:

    fetch_task = PythonOperator(

        task_id="fetch_employee_data",

        python_callable=fetch_employee_data,

    )