# Django Management Commands

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