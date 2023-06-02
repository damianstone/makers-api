# Makers
A simple API built using Django REST and deployed on Heroku, using a bucket (AWS S3) to host the images and a PostgreSQL database to store the data.

## Initialization

#### Create a virtual environment

```python
python3 -m venv venv-api
source venv-api/bin/activate
```

#### Install requirements.txt

```python
pip install -r requirements.txt
```

#### Create superuser

```python
python manage.py createsuperuser
```

#### Add PostgreSQL db 
Then, create an `.env` file  and add the following to connect your local database
 
```bash
LOCAL_DB_NAME=db-name
LOCAL_DB_USER=
LOCAL_DB_PASSWORD=
LOCAL_DB_HOST=127.0.0.1
LOCAL_DB_PORT=5432
```

#### Migrate models

```python
python manage.py makemigrations
python manage.py migrate
```

#### Run

```python
python manage.py runserver
```
