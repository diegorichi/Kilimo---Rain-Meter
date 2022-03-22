

del .\my-local-sqlite.db
rmdir -r rain\migrations\

python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py migrate --run-syncdb

python .\manage.py createsuperuser --username admin --email admin@kilimo.com
