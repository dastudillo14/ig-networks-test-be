from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F

from user.permissions import IsAdminGroup
from .models import JobPost
from .serializers import JobPostReadSerializer, JobPostWriteSerializer
from .filters import JobPostFilter

permissions = [IsAdminGroup , IsAuthenticated]  # Permissions for the viewset


class JobPostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing job post instances.
    """
    # Allow filtering through the fields defined in JobPostFilter
    filter_backends = (DjangoFilterBackend,)
    filterset_class = JobPostFilter  # Using the filter we created

    queryset = JobPost.objects.all().order_by(F('created_at').desc())

    # Use different serializer depending on the HTTP method
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET methods
            return JobPostReadSerializer
        return JobPostWriteSerializer  # POST/PUT/PATCH methods

    def create(self, request, *args, **kwargs):
        created_by_id = request.user.id
        request.data['created_by'] = created_by_id
        self.permission_classes = permissions
        self.check_permissions(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        created_by_id = request.user.id
        request.data['created_by'] = created_by_id
        self.permission_classes = permissions
        self.check_permissions(request)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.permission_classes = permissions
        self.check_permissions(request)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = permissions
        self.check_permissions(request)
        instance = self.get_object()
        if(instance.active == False):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
