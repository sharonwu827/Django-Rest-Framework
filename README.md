# Django

Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python (3.5, 3.6, 3.7, 3.8, 3.9)
- Django (2.2, 3.0, 3.1, 3.2)

## Installation
```python
pip install djangorestframework

# Add 'rest_framework' to your INSTALLED_APPS setting.
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Django Management Commands

```python
# Create new Django project
django-admin.py startproject profiles_project  .
# Create new Django app
python manage.py startapp profiles_api
# Start Django development server
python manage.py runserver 0.0.0.0:8000
# Create database migrations file
python manage.py makemigrations
# Run migrations
python manage.py migrate
# Create new superuser
python manage.py createsuperuser
```