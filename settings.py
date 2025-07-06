import os
MAIL_FROM = 'noreply@example.com'
TEST_MAIL_TO = ['test@example.com']
#DIR = os.path.abspath('reports')
PYODBC_CONNECTOR = (
    "DRIVER={driver};"
    "DATABASE={database};"
    "UID={user};"
    "PWD={password};"
    "SERVER={host};"
    "PORT={port};"
)
POSTGRESS_CONNECTOR = 'pq://{user}:{password}@{host}:{port}/{database}'
# TODO
REPLICA_CONNECTION = {
    'host': 'db-host.example.com',
    'port': '5432',
    'user': 'non-secret-user',
    'password': 'kjCWFuvjbRrCC9C57qFALz0yO6EO9sfv',
    'database': 'database',
}

CLICKHOUSE_CONNECTION = {
    'host': 'clickhouse.example.com',
    'port': 9000,
    'user': 'secretuser',
    'password': 'qG1Rv9gp5jOgffMN1xvjb4o',
    'database': 'octoberfest',
}
