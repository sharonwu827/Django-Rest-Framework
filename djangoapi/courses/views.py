from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializier


# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializier








