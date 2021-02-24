from datetime import timedelta
import logging

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.utils.dates import days_ago

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'sara',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['sara@acloudfrontier.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

# define the DAG
dag = DAG(
    'connection_snowflake',
    default_args=default_args,
    description='First example with snowflake connection running',
    schedule_interval=None,
)


snowflake_query = [
    """create table public.test_employee (id number, name string);""",
    """insert into public.test_employee values(1, 'Sam'),(2, 'Andy'),(3, 'Gill');""",
]

# define the first task (will call the snowflake_query)
create_insert = SnowflakeOperator(
    task_id='snowflake_create',
    sql=snowflake_query,
    snowflake_conn_id="snowflake_conn",
    dag=dag,
)

# task pipeline
create_insert