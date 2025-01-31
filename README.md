# Sav_Test


Setup Project:
Steps:
1) git clone https://github.com/dumoresagar/Sav_Test.git
2) pip install virtualenv
3) python -m venv venv
4) source venv/bin/activate 
5) cd TIMESTAMP
6) pip install -r rerequirements.txt
7) celery -A Timestamps worker --loglevel=info & python manage.py runserver &
