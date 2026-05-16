import os

# ---------------------------------
# Superset Secret Key
# ---------------------------------
SECRET_KEY = "my_super_secret_key_123456789"


# ---------------------------------
# PostgreSQL Connection
# ---------------------------------
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:Postgres123456@postgres:5432/postgres"
)


# ---------------------------------
# Disable CSRF for Local Development
# ---------------------------------
WTF_CSRF_ENABLED = False


# ---------------------------------
# Enable Proxy Fix
# ---------------------------------
ENABLE_PROXY_FIX = True


# ---------------------------------
# Dashboard Row Limit
# ---------------------------------
ROW_LIMIT = 5000


# ---------------------------------
# Cache Config (Optional)
# ---------------------------------
CACHE_CONFIG = {
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300
}