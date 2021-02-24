from datetime import timedelta
import logging

from airflow import DAG
import os
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from airflow.utils.email import send_email


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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


def notify_email(contextDict, **kwargs):
    task_instance = contextDict['task_instance']
    task_id = task_instance.task_id
    log_id = task_instance.log_url
    data_docs_url = "file:///Users/sara/airflow/dags/snowflake/great_expectations/uncommitted/data_docs/local_site/index.html"

    # email title.
    title = "Airflow alert: "+task_id+" Failed".format(**contextDict)

    # email contents
    body = """
    Hi Everyone, <br>
    <br>
    There's been an error in the """+task_id+""" job.<br>
    <br>
    Airflow bot <br>
    """.format(**contextDict)

    send_email('sara@acloudfrontier.com', title, body)


dag = DAG(
    dag_id='ge_bash_op_dag',
    default_args=default_args,
    description='Run checkpoints',
    schedule_interval=timedelta(days=1),
)



data_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local')
snowflake_query1 = ["""put file:///"""+data_root_dir+"""/yellow_tripdata_sample_2019-01.csv @%monthly_data;""",
"""copy into monthly_data from '@%monthly_data/yellow_tripdata_sample_2019-01.csv.gz' ;""",]
import_monthly_data = SnowflakeOperator(
    task_id='import_monthly_data',
    sql=snowflake_query1,
    snowflake_conn_id="SNOWFLAKE_CONN_DEMO",
    dag=dag,
)

ge_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snowflake')
val_monthlychk = BashOperator(
    task_id='Val_monthlychk',
    bash_command='cd '+ge_root_dir+' && great_expectations checkpoint run monthlychk',
    on_failure_callback=notify_email,
    dag=dag
)

snowflake_query2 = ["""insert into  GENERIC_NYC_TAXI select * from MONTHLY_DATA;""",]
copy_to_generic_table = SnowflakeOperator(
    task_id='copy_to_generic_table',
    sql=snowflake_query2,
    snowflake_conn_id="SNOWFLAKE_CONN_DEMO",
    dag=dag,
)

snowflake_query3 = ["""delete from MONTHLY_DATA;""",]
drop_monthly_data = SnowflakeOperator(
    task_id='drop_monthly_data',
    sql=snowflake_query3,
    snowflake_conn_id="SNOWFLAKE_CONN_DEMO",
    dag=dag,
)

import_monthly_data >> val_monthlychk >> copy_to_generic_table >> drop_monthly_data

