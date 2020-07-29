# Adai Serve


`C:\User\` git clone [https://github.com/uagrm-sw1/adai-serve.git](https://github.com/uagrm-sw1/adai-serve.git)

## Local 

`C:\User\` cd Carpte_del_Repositorio (Carp)

`C:\User\Carp\` venvadai\Scripts\activate

`(venvadai) C:\User\Carp\` pip install -r requirements.txt

** MIGRACIONES **

`(venvadai) C:\User\Carp\` python manage.py makemigrations

`(venvadai) C:\User\Carp\` python manage.py migrate

`(venvadai) C:\User\Carp\` python manage.py runserver

## Deploy Changes

git commit y git push

Open `Git Bash` on Terminal

`~` ssh ubuntu@ec2-3-134-80-247.us-east-2.compute.amazonaws.com

`ubuntu@ip-nnn-nn-nn-nn:~` sudo -i

`root@ip-nnn-nn-nn-nn:~#`cd /usr/local/apps/adai-serve/

`root@__:~/adai-serve#` source /usr/local/apps/adai-serve/env/bin/activate

`(env) root@__:~/adai-serve#` sudo ./deploy/update.sh