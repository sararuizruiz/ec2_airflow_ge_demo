from datetime import timedelta
import logging

from airflow import DAG
import os
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago
# from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
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
    dag_id='docker_ge_quarantine_dag',
    default_args=default_args,
    description='Run checkpoints',
    schedule_interval=None,
)



data_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local')
snowflake_query1 = ["""put file:///"""+data_root_dir+"""/yellow_tripdata_sample_2019-03.csv @%raw_monthly_taxi;""",
"""copy into raw_monthly_taxi from '@%raw_monthly_taxi/yellow_tripdata_sample_2019-03.csv.gz' ;""",
"""alter table RAW_MONTHLY_TAXI add column GE_validation_result integer;""",] 
import_raw_monthly_data = SnowflakeOperator(
    task_id='import_raw_monthly_data',
    sql=snowflake_query1,
    snowflake_conn_id="SNOWFLAKE_QUARANTINE_DEMO",
    dag=dag,
)

ge_root_dir = "/home/ec2-user/airflow"
requirements_dir = ge_root_dir+"/requirements.txt:/requirements.txt"
ge_dir = ge_root_dir+"/dags/snowflake/quarantine_df/great_expectations:/usr/app/great_expectations"


def print_context():
        print(ge_dir)
LOGGER = logging.getLogger("airflow.task")
LOGGER.info("airflow.task >>> 2 - INFO logger test")
LOGGER.info('ge dir %s', ge_dir)
LOGGER.info('requirements dir %s', requirements_dir)
ge_val_monthlychk = DockerOperator(
       task_id="GE_validation",
       image="hacked_ge_image",
       command="checkpoint run monthlychk",
#       docker_url="unix://var/run/docker.sock",
       volumes=[ge_dir,requirements_dir],
#       on_failure_callback=notify_email,
       dag=dag
   )


snowflake_query5 = [
"""insert into  ABT_NYC_TAXI select * from RAW_MONTHLY_TAXI where GE_validation_result is NULL;""",
]

import_valid_records = SnowflakeOperator(
    task_id='import_valid_records',
    sql=snowflake_query5,
    snowflake_conn_id="SNOWFLAKE_QUARANTINE_DEMO",
    dag=dag,
    trigger_rule='all_done',
)


snowflake_query4 = [
"""insert into  QUARANTINE_DATA select * from RAW_MONTHLY_TAXI where GE_validation_result=1;""",
]

import_invalid_records = SnowflakeOperator(
    task_id='import_invalid_records',
    sql=snowflake_query4,
    snowflake_conn_id="SNOWFLAKE_QUARANTINE_DEMO",
    dag=dag,
    trigger_rule='all_failed',
)


snowflake_query3 = ["""alter table RAW_MONTHLY_TAXI drop column GE_validation_result;""",
    """delete from RAW_MONTHLY_TAXI;""",]
clean_up_monthly_data = SnowflakeOperator(
    task_id='clean_up_monthly_data',
    sql=snowflake_query3,
    snowflake_conn_id="SNOWFLAKE_QUARANTINE_DEMO",
    dag=dag,
    trigger_rule='one_success',
)





import_raw_monthly_data >> ge_val_monthlychk 
ge_val_monthlychk >> import_valid_records >> clean_up_monthly_data
ge_val_monthlychk >> import_invalid_records >> clean_up_monthly_data
