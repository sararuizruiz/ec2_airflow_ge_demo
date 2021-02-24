docker
sudo yum update -y
sudo amazon-linux-extras install docker
docker ps
sudo service docker start
docker ps
sudo docker ps
usermod -aG sudo ec2-user
sudo usermod -aG sudo ec2-user
logout
docker
docker ps
sudo usermod -aG docker $USER
sudo su -
logout
scp -r $HOME/airflow acf_ge_demo:/home/ec2-user/
docker run -d -p 8080:8080 -v $PWD/airflow/dags/:/usr/local/airflow/dags -v $PWD/airflow/requirements.txt:/requirements.txt -v /var/run/docker.sock:/var/run/docker.sock puckel/docker-airflow webserver
logout
docker run -d -p 8080:8080 -v $PWD/airflow/dags/:/usr/local/airflow/dags -v $PWD/airflow/requirements.txt:/requirements.txt -v /var/run/docker.sock:/var/run/docker.sock puckel/docker-airflow webserver
docker load < hacked_ge_image.tar
docker list
docker ps
docker exec -it objective_yalow bash
docker exec -it -u root objective_yalow bash
docker os
docker ps
docker ps
docker exec -it objective_yalow bash
docker exec -it -u root objective_yalow bash
docker exec -it objective_yalow bash
docker exec -it -u root objective_yalow bash
sudo groupadd docker
sudo usermod -aG docker airflow
docker restart objective_yalow
docker ps
docker run -d -p 8080:8080 -v $PWD/airflow/dags/:/usr/local/airflow/dags -v $PWD/airflow/requirements.txt:/requirements.txt -v /var/run/docker.sock:/var/run/docker.sock puckel/docker-airflow webserver
docker exec -it -u root objective_yalow bash
docker ps
sudo docker ps
sudo docker exec -it objective_yalow bash
sudo docker restart objective_yalow
ls
cd airflow
ls
cd dags
ls
nano docker_ge_quarantine_dag.py
ls
cd demo
ls
cd ..
ls
nano docker_ge_quarantine_dag.py
docker ps
sudo docker ps
nano docker_ge_quarantine_dag.py
ls
cd demo
ls
cd great_expectations
ls
cd ..
ls
nano docker_ge_quarantine_dag.py
docker ps

sudo docker exec -it objective_yalow bash
echo $pwd
echo $PWD
nano docker_ge_quarantine_dag.py
cd ..
ls
cd dags/snowflake/quarantine_df/great_expectations/
cd uncommitted/data_docs/
ls
cd local_site/
ls
index.html
safari index.html
open index.html
open ./index.html
open index.html
xdg-open index.html
xdg-open ./index.html
which xdg-open
sudo xdg-open index.html
sudo xdg-open ./index.html
sudo apt-get install lynx
sudo xdg-open index.html
sudo apt-get install --reinstall xdg-utils
sudo yum install --reinstall xdg-utils
sudo yum install xdg-utils
sudo xdg-open index.html
sudo xdg-open ./index.html
sudo yum install lynx
sudo lynx ./index.html
safari index.html
sudo xdg-open index.html
sudo xdg-open ./index.html
google-chrome index.html
open -a "google\ chrome.app" index.html
sudo xdg-open index.html
pwd
ls
ls airflow/dags/snowflake/quarantine_df/great_expectations/uncommitted/data_docs/local_site/
docker ps
sudo docker ps
docker exec -it objective_yalow bash
sudo docker exec -it objective_yalow bash
sudo docker exec -it -u root objective_yalow bash
cd airflow/dags/snowflake/quarantine_df/great_expectations/uncommitted/
ls -l
cd data_docs/local_site/
python3 -m http.server
yum install -y python3
yum install -y python
sudo yum install -y python3
python3 -m http.server
docker os

sudo docker os
sudo docker ps
mkdir www
sudo docker exec -it objective_yalow bash
sudo docker exec -it -u root objective_yalow bash
sudo docker cp -r objectivre_yelow:/usr/local/lib/python3.7/site-packages/airflow/www $PWD/www
sudo docker cp objectivre_yelow:/usr/local/lib/python3.7/site-packages/airflow/www $PWD/www
sudo docker cp objectivre_yelow:/usr/local/lib/python3.7/site-packages/airflow/www/ $PWD/www
sudo docker ps
sudo docker cp objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/ $PWD/www
ls -l
cd www/
ls -l
sudo docker exec -it -u root objective_yalow bash
nano www/templates/admin/master.html 
sudo nano www/templates/admin/master.html 
sudo docker ps
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
git
apt install -y git
sudo nano www/templates/admin/master.html 
sudo docker cp www/templates/admin/master.html objective_yalow:/usr/local/lib/python3.7/site-packages/airflow/www/templates/admin/master.html
cd airflow/dags/snowflake/quarantine_df/great_expectations/uncommitted/data_docs/local_site/
python3 -m http.server
cd ~
ls 
nano run_ge_webserver.sh
bash run_ge_webserver.sh 
ps aux | grep http
ps aux
ps aux | grep http
kill 934
bash run_ge_webserver.sh 
mkdir docker
cd docker/
nano Dockerfile.airflow
docker build -t acf/airflow -f Dockerfile.airflow .
sudo docker build -t acf/airflow -f Dockerfile.airflow .
docker run --name acf_airflow -p 9080:8080 acf/airflow:latest webserver
echo "sudo docker build -t acf/airflow -f Dockerfile.airflow ." > build.sh
cat build.sh 
sudo docker run --name acf_airflow -p 9080:8080 acf/airflow:latest webserver
nano navbar_menu.html
nano run.sh
bash run.sh 
docker rm -f acf_airflow
nano run.sh 
bash run.sh 
sudo docker exec -it acf_airflow bash
nano run.sh 
bash run.sh 
sudo docker exec -it acf_airflow bash
nano navbar_menu.html 
bash run.sh 
nano run.sh 
bash run.sh 
docker logs -f acf_airflow
sudo docker logs -f acf_airflow
sudo docker exec -it acf_airflow bash
ls $USER
ls $HOME
nano run.sh 
bash run.sh 
nano run.sh 
bash run.sh 
nano navbar_menu.html 
bash run.sh 
cd ..
ls -l
bash run_ge_webserver.sh 
ps aux | grep http
kill 4203
ps aux | grep http
bash run_ge_webserver.sh 
ps aux | grep http
kill 29292
nano run_ge_webserver.sh 
bash run_ge_webserver.sh 
cd docker/
ls -l
nano navbar_menu.html 
nano run.sh 
ls
cd ww
cd www
ls
cd www/
ls
cd static
ls
nano test.html
ls
cd ..
ls
cd templates/
ls
cd airflow/
ls
nano dag.html
cd
ls
nano run_ge_webserver.sh 
ls
cd airflow/dags/
ls
nano docker_ge_quarantine_dag.py 
cd snowflake/quarantine_df/
ls
great_expectations suite edit taxisuite
suite edit taxi suite
ls
cd great_expectations/uncommitted/
ls
open edit_taxisuite.ipynb
jupyter notebook edit_taxisuite.ipynb
nano jupyter notebook edit_taxisuite.ipynb
sudo jupyter notebook edit_taxisuite.ipynb
wich python3
which puthon3
which python3
which pip3
pip3 install jupyter
jupyter notebook edit_taxisuite.ipynb
pip3 install jupyter
clean
clear
cd
cd airflow/dags/
nano docker_ge_quarantine_dag.py 
docker ps
sudo docker ps
sudo docker exec -it root acf_airflow bash
sudo docker exec -it -u root acf_airflow bash
cd docker/
nano init_security.py
nao run.sh 
nano run.sh 
bash run.sh 
cd ..
ls -l
cp -r airflow airflow_2
ls -l
ls -l airflow_2
cd docker/
nano run.sh 
bash run.sh
nano run.sh 
bash run.sh
nano run.sh 
sudo docker exec -it -u root acf_airflow bash
nano run.sh 
sudo docker exec -it -u root acf_airflow bash
nano run.sh 
bash run.sh
nano run.sh 
bash run.sh
sudo docker exec -it -u root acf_airflow bash
sudo docker cp acf_airflow:/root/airflow/airflow.cfg airflow.cfg
nano airflow.cfg 
nano run.sh
nano airflow.cfg 
sudo nano airflow.cfg 
sudo chmod 777 airflow.cfg 
bash run.sh
nano run
nano run.sh
bash run.sh
nano airflow.cfg 
nano run.sh
bash run.sh
sudo docker exec -it -u root acf_airflow bash
nano run.sh
bash run.sh
sudo docker exec -it -u root acf_airflow bash
nano run.sh
nano startup.sh
nano run.sh
nano Dockerfile.airflow
nano entrypoint.sh
nano Dockerfile.airflow 
bash build.sh 
bash run.sh
docker logs -f acf_airflow
sudo docker logs -f acf_airflow
nano entrypoint.sh 
bash build.sh 
bash run.sh
sudo docker logs -f acf_airflow
nano entrypoint.sh 
nano run.sh
bash build.sh 
bash run.sh
sudo docker logs -f acf_airflow
sudo docker exec -it -u root acf_airflow bash
nano Dockerfile.airflow 
bash build.sh 
bash run.sh
sudo docker logs -f acf_airflow
nano ~/airflow_2/requirements.txt 
bash run.sh
sudo docker logs -f acf_airflow
nano ~/airflow_2/requirements.txt 
bash run.sh
sudo docker logs -f acf_airflow
nano Dockerfile.airflow 
bash build.sh 
nano ~/airflow_2/requirements.txt 
bash run.sh
sudo docker logs -f acf_airflow
nano run.sh
bash run.sh
sudo docker logs -f acf_airflow
cat Dockerfile.airflow 
sudo docker logs -f acf_airflow
nano run.sh
bash run.sh
sudo docker logs -f acf_airflow
ls
ls airflow_2
nano webserver_config.py
cd
cd www
ls
cd www
ls
cd templates/
ls
cd admin/
ls
nano master.html
cd
ls
cd airflow_2
ls
cd 
cd www/www/
ls
cd templates/
cd airflow/
ls
nano master.html
cd
ls
cd airflow_2
ls
cd
ls
cd airflow
ls
cd 
cd www/
ls
cd www/
ls
cd templates/
ls
cd admin/
ls
nano master.html
ls
cd
ls
cd docker
ls
nano navbar_menu.html 
bash run.sh
cd
ls
cd airflow_2
ls
cd
cd airflow/dags/snowflake/quarantine_df/great_expectations/uncommitted/
ls
rm run_monthlychk.py 
ls
bash run.sh
cd
bash run.sh
cd airflow
ls
cd dags/snowflake/quarantine_df/great_expectations/uncommitted/
ls
cd
bash run.sh
cd airflow_2/dags/snowflake/quarantine_df/great_expectations/uncommitted/
ls
rm run_monthlychk.py 
ls
bash run.py
bash run.sh
cd
cd docker/
nano navbar_menu.html 
bash run.sh
nano run.sh
bash run.sh
