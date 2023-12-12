# vendor-management

## Installation

1. **First clone the repository in your system.**

   `https://github.com/swalih2233/vendor-management.git`

2. **Then start Virtual Environment within current Directory.**

   `python -m venv venv`

   `venv\Scripts\activate`

3. **Then install the dependencies from requirements.txt.**

   `pip install -r requirements.txt`


4. **Then change the DB Details in settings.py**

   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'DB_NAME',
         'USER':'DB_USER',
         'PASSWORD':'DB_USER_PASSWORD',
         'HOST':'localhost',
         'PORT':'5432'
      }
   }
   
5. **Then Apply Migrations.**

   `python manage.py makemigrations`

   `python manage.py migrate`

6. **Execute the manage.py file to runserver.**

   `python manage.py runserver`

7. **Then Goto your favourite Browser and Type in localhost:8000.**