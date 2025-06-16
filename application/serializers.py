from rest_framework import serializers

from status.serializers import StatusSerializer
from jobpost.models import JobPost
from jobpost.serializers import JobPostReadSerializer, SimpleJobPostSerializer
from user.serializers import SimpleUserSerializer
from application.models import Application
from django.contrib.auth.models import User


# Main serializer for reading (GET)
class ApplicationReadSerializer(serializers.ModelSerializer):
    applicant = SimpleUserSerializer()  # For GET, show complete user details
    jobpost = SimpleJobPostSerializer()  # For GET, show complete JobPost details
    status = StatusSerializer()
    class Meta:
        model = Application
        fields = '__all__'

       
# Serializer for creation/update (POST/PUT/PATCH)
class ApplicationWriteSerializer(serializers.ModelSerializer):
    # Using PrimaryKeyRelatedField to allow sending only the ID
    applicant = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    jobpost = serializers.PrimaryKeyRelatedField(queryset=JobPost.objects.all())

    class Meta:
        model = Application
        fields = '__all__'       