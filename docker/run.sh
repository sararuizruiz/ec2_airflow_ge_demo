sudo docker rm -f acf_airflow || true

sudo docker run -d \
	--name acf_airflow \
	-p 9080:8080 \
	-v $PWD/navbar_menu.html:/usr/local/lib/python3.7/site-packages/airflow/www/templates/appbuilder/navbar_menu.html \
	-v $PWD/init_security.py:/usr/local/lib/python3.7/site-packages/airflow/www/extensions/init_security.py \
	-v $PWD/airflow.cfg:/root/airflow/airflow.cfg \
	-v ~/airflow/dags/snowflake/quarantine_df/great_expectations/uncommitted/data_docs/local_site:/usr/local/lib/python3.7/site-packages/airflow/www/static/great_expectations \
        -v ~/airflow_2/dags:/root/airflow/dags \
	-v ~/airflow_2/requirements.txt:/requirements.txt \
	-v /var/run/docker.sock:/var/run/docker.sock \
	acf/airflow:latest webserver
