from rest_framework import serializers
from .models import Course


class CourseSerializier(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "url","name","language","price")

