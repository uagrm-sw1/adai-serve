
git clone https://github.com/uagrm-sw1/adai-serve.git

cd Carpte_del_Repositorio

venvadai\Scripts\activate

pip install -r requirements.txt

/------------MIGRACIONES---------/
python manage.py makemigrations
python manage.py migrate
/--------------------------------/

python manage.py runserver