Weather App
Project for retrieve weather status and forecast using https://openweathermap.org/ API

The API End points are protected using JWT authenication. And could be accessed as well if you are logged using session.

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

# Run the server
python manage.py runserver
Then you could access the gui in the browser on http://localhost:8000/

# Run test
 python manage.py test

IMPORTANT: Get the apikey by creating a free account in https://openweathermap.org/. You will be asked for it when app starts.

Built With DJANGO and DjangoRestFramework

By Andrés López 