

from datetime import timedelta

from airflow import DAG
import os
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

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
    'ge_local_dag',
    default_args=default_args,
    description='Run GE on local data',
    schedule_interval=timedelta(days=1),
)

ge_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local/great_expectations')
data_file_01 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local/yellow_tripdata_sample_2019-01.csv')
data_file_02 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local/yellow_tripdata_sample_2019-02.csv')
data_file_03 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local/yellow_tripdata_sample_2019-03.csv')

ge_val_01 = GreatExpectationsOperator(
    task_id='ge_val_01',
    expectation_suite_name='taxisuite',
    batch_kwargs={
        'path': data_file_01,
        'datasource': 'my_local_db'
    },
    data_context_root_dir=ge_root_dir,
    dag=dag
)

ge_val_02 = GreatExpectationsOperator(
    task_id='ge_val_02',
    expectation_suite_name='taxisuite',
    batch_kwargs={
        'path': data_file_02,
        'datasource': 'my_local_db'
    },
    data_context_root_dir=ge_root_dir,
    dag=dag
)

ge_val_03 = GreatExpectationsOperator(
    task_id='ge_val_03',
    expectation_suite_name='taxisuite',
    batch_kwargs={
        'path': data_file_03,
        'datasource': 'my_local_db'
    },
    data_context_root_dir=ge_root_dir,
    dag=dag
)



ge_val_01 >> ge_val_02 >> ge_val_03