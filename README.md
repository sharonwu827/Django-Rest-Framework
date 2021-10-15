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


## Example 

A quick example of using REST framework to build a simple model-backed API for 
accessing users and groups.

**Startup up a new project**

```python
pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
```
**Now edit the example/urls.py module in the project**
```python
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

We'd also like to configure a couple of settings for our API. 
Add the following to your settings.py module:

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
```



