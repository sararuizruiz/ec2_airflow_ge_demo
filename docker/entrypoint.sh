#!/bin/bash

pip install -r /requirements.txt || true

airflow scheduler &
airflow $@
