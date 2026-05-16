````markdown
# Employee Data Quality Monitoring Platform

## 📌 Project Overview

This project is an enterprise-grade **Employee Data Quality Monitoring Platform** built using:

- Apache NiFi → Data ingestion
- Apache Airflow → Workflow orchestration & scheduling
- Python Validation Engine → Data quality checks
- MLflow → Metrics tracking
- PostgreSQL → Data storage
- Apache Superset → Dashboards & KPI visualization

---

# 🎯 Project Goal

Build an automated employee data quality monitoring system that:

✅ Runs every 12 hours  
✅ Validates employee data quality  
✅ Stores validation metrics in PostgreSQL  
✅ Logs metrics using MLflow  
✅ Visualizes KPIs in Apache Superset  

---

# 🔄 End-to-End Pipeline Flow

DummyJSON Employee API  
⬇  
Apache NiFi  
⬇  
Apache Airflow  
⬇  
Validation Engine (Python)  
⬇  
MLflow Tracking  
⬇  
PostgreSQL  
⬇  
Apache Superset Dashboard  

---

# 📁 Project Structure

```text
EmployeeDataQuality/
│
├── Airflow/
│   ├── airflow.db
│   └── logs/
│
├── venv/
│
├── database/
│   └── employee_dq_schema.sql
│
├── ingestion/
│   └── fetch_employee_data.py
│
├── validation_engine/
│   ├── __init__.py
│   ├── validator.py
│   └── rules.py
│
├── mlflow_tracking/
│   └── mlflow_utils.py
│
├── dags/
│   └── validator_dag.py
│
├── superset_dashboards/
│   └── employee_quality_dashboard.json
│
├── config/
│   └── db_config.py
│
├── requirements.txt
│
└── README.md
````

---

# ⚙️ Technologies Used

| Tool            | Purpose                 |
| --------------- | ----------------------- |
| Apache NiFi     | Data ingestion          |
| Apache Airflow  | Workflow scheduling     |
| PostgreSQL      | Database                |
| Python          | Validation logic        |
| MLflow          | Metrics tracking        |
| Apache Superset | Dashboards              |
| VSCode          | Development environment |

---

# 🐍 Python Environment Setup

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 2️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 PostgreSQL Setup

## Create Database

```sql
CREATE DATABASE employee_dq;
```

---

## Run Schema File

Execute:

```text
database/employee_dq_schema.sql
```

This creates:

* dummy_users
* validation_results
* dq_metrics
* pipeline_runs
* mlflow_metrics

---

# 🌬 Apache Airflow Setup

## Set AIRFLOW_HOME

### Windows CMD

```bash
set AIRFLOW_HOME=E:\EmployeeDataQuality\Airflow
```

---

## Configure PostgreSQL Connection

Update:

```text
Airflow/airflow.cfg
```

Find:

```ini
sql_alchemy_conn =
```

Replace with:

```ini
sql_alchemy_conn = postgresql+psycopg2://postgres:Postgres123456@localhost:5432/employee_dq
```

---

## Initialize Airflow Database

```bash
airflow db init
```

---

# ▶ Run Airflow

## Start Webserver

```bash
airflow webserver --port 8080
```

---

## Start Scheduler

Open another terminal:

```bash
airflow scheduler
```

---

# 🌐 Access Airflow UI

Open browser:

```text
http://localhost:8080
```

---

# ✅ Validation Engine

The validation engine checks:

* Missing emails
* Invalid email format
* Salary range
* Age range

Validation results are stored in:

```text
validation_results
```

Metrics stored in:

```text
dq_metrics
```

---

# 📊 MLflow Tracking

MLflow logs:

* total_checked
* fail_null
* fail_email
* fail_salary
* fail_age
* pass_all

---

## Run MLflow UI

```bash
mlflow ui
```

Open:

```text
http://localhost:5000
```

---

# 📈 Apache Superset Dashboard

Dashboard shows:

✅ % valid employee records
✅ Failed validations by type
✅ Missing values trend
✅ Pipeline run history
✅ Validation trends over time

---

# 📊 Recommended Dashboard Charts

| Chart                    | Purpose     |
| ------------------------ | ----------- |
| % Valid Records          | KPI         |
| Failed Validation Counts | Bar chart   |
| Missing Values Trend     | Line chart  |
| Pipeline Run Logs        | Table       |
| Validation Trends        | Time series |

---

# ⏰ Airflow DAG Schedule

The DAG runs every 12 hours:

```python
schedule_interval='0 */12 * * *'
```

---

# 🚀 Run the Validation DAG

Place DAG file in:

```text
dags/validator_dag.py
```

Airflow automatically detects it.

---

# 📌 Main Features

✅ Automated validation
✅ PostgreSQL integration
✅ Airflow scheduling
✅ MLflow metric tracking
✅ Apache Superset dashboards
✅ Enterprise-grade architecture

---

# 🔮 Future Enhancements

* Real-time streaming validation
* Email alerts on failures
* Slack/MS Teams integration
* Great Expectations integration
* Docker deployment
* Kubernetes orchestration

---

# 👨‍💻 Author
 Name: Bilal Mohammad Afzal
Employee Data Quality Monitoring Platform

Built using:
Apache NiFi + Apache Airflow + PostgreSQL + MLflow + Apache Superset

```
```
                    