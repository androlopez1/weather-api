Weather App
Project for retrieve weather status and forecast using https://openweathermap.org/ API

Users must be logged in in order to make request.

# Create a virtualenv 
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install project requirements
pip install -r requirements.txt

# Run the migrations
cd src
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
http://localhost:8000/

# Run test
 python manage.py test
 
# URL:
Login: localhost:8000 
Users Api: /users 

IMPORTANT: Get the apikey by creating a free account in https://openweathermap.org/. You will be asked for it when app starts.

Built With DJANGO and DjangoRestFramework

By Andrés López 
