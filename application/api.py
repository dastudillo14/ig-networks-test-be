from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import F

from application.filters import ApplicationFilter
from user.permissions import IsAdminGroup, IsApplicantGroup
from application.models import Application
from .serializers import ApplicationReadSerializer, ApplicationWriteSerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from constants import APPLICANT_ROLE

permissions = [ IsAuthenticated ]  # Permissions for the viewset


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Application instances.
    """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ApplicationFilter  # Using the filter we created

    queryset = Application.objects.all()


    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET methods
            return ApplicationReadSerializer
        return ApplicationWriteSerializer  # POST, PUT, PATCH methods
    
    def get_queryset(self):
        user = self.request.user
        self.permission_classes = permissions
        self.check_permissions(self.request)
        qs = self.queryset
        if user.groups.filter(name=APPLICANT_ROLE).exists():
            qs = qs.filter(applicant=user)
    
        return qs.order_by(F('submission_date').desc())
    
    def create(self, request, *args, **kwargs):
        self.permission_classes = permissions
        self.check_permissions(request)
        
        applicant_id = request.user.id

        if Application.objects.filter(jobpost_id= request.data['jobpost'] , applicant_id= applicant_id).exists():
            return Response({'error': 'You have already applied for this job.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Set the applicant to the current user
        request.data['applicant'] = applicant_id
        
        return super().create(request, *args, **kwargs)