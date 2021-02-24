from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
# from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'sara',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['sara@acloudfrontier.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
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
    'first_dag',
    default_args=default_args,
    description='First example to get Live Cricket Scores',
    schedule_interval=None,
)

# define the first task
t1 = BashOperator(
    task_id='print',
    bash_command='echo Getting Live Cricket Scores!!!',
    dag=dag,
)


# define the second task
t2 = BashOperator(
    task_id='print2',
    bash_command='echo not!!!',
    dag=dag,
)

# task pipeline
t1 >> t2