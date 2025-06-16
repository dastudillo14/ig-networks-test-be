from rest_framework import serializers

from user.serializers import SimpleUserSerializer
from category.serializers import CategorySerializer
from .models import JobPost
from category.models import Category
from django.contrib.auth.models import User



# Main serializer for reading (GET)
class JobPostReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # For GET, show complete category details
    created_by = SimpleUserSerializer()  # For GET, show complete user details

    class Meta:
        model = JobPost
        fields = '__all__'

# Serializer for creation/update (POST/PUT/PATCH)
class JobPostWriteSerializer(serializers.ModelSerializer):
    # Using PrimaryKeyRelatedField to allow sending only the ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = JobPost
        fields = '__all__'


class SimpleJobPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # For GET, show complete category details

    """
    Simple serializer for JobPost, used in ApplicationReadSerializer.
    """
    class Meta:
        model = JobPost
        fields = ['id', 'title', 'location','category']  # Fields to show in the simple serializer
