virtualenv env  
env/bin/activate  
pip install requirements.txt  

python manage.py makemigrations rest  
python manage.py migrate rest  

python manage.py runserver

API at http://127.0.0.1:8000/tasks
