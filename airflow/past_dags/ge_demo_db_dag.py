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
    dag_id='ge_demo_db_dag',
    default_args=default_args,
    description='Run checkpoint against the three tables in ge_demo_db (snowflake)',
    schedule_interval=timedelta(days=1),
)

ge_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snowflake/ge_demo_db')


check_expectation_suite = BashOperator(
    task_id='check_expectation_suite',
    bash_command='cd '+ge_root_dir+' && great_expectations docs build -y',
    on_success_callback= lambda: time.sleep(300),
    dag=dag,
)

run_checkpoint = BashOperator(
    task_id='run_checkpoint',
    bash_command='cd '+ge_root_dir+' && great_expectations checkpoint run monthlychk',
    on_failure_callback=notify_email,
    dag=dag
)

check_results = BashOperator(
    task_id='check_results',
    bash_command='cd '+ge_root_dir+' && great_expectations docs build -y',
    dag=dag,
    trigger_rule='all_done',
)

check_expectation_suite >> run_checkpoint >> check_results

