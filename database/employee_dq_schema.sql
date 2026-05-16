-- ===========================================
-- Employee Data Quality Monitoring Platform
-- Clean PostgreSQL Schema (Production Ready)
-- ===========================================

-- ===========================================
-- 1. Employee Data Quality Checks
-- ===========================================
CREATE TABLE IF NOT EXISTS validation_results (
    id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    check_name VARCHAR(150) NOT NULL,
    status VARCHAR(20) NOT NULL,  -- PASS / FAIL
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_validation_employee ON validation_results(employee_id);
CREATE INDEX idx_validation_status ON validation_results(status);


-- ===========================================
-- 2. Data Quality Metrics (Aggregated)
-- ===========================================
CREATE TABLE IF NOT EXISTS dq_metrics (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(100) NOT NULL,
    metric_value DOUBLE PRECISION NOT NULL,
    run_id VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dq_metrics_run ON dq_metrics(run_id);


-- ===========================================
-- 3. Pipeline Execution Logs
-- ===========================================
CREATE TABLE IF NOT EXISTS pipeline_runs (
    id SERIAL PRIMARY KEY,
    run_id VARCHAR(100) UNIQUE,
    run_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_records INT NOT NULL DEFAULT 0,
    passed_records INT NOT NULL DEFAULT 0,
    failed_records INT NOT NULL DEFAULT 0,
    status VARCHAR(20) DEFAULT 'SUCCESS'
);

CREATE INDEX idx_pipeline_run_id ON pipeline_runs(run_id);