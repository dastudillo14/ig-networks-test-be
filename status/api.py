from rest_framework import viewsets
from .models import Status
from status.serializers import StatusSerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing status instances.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer