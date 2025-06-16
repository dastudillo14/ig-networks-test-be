from rest_framework.routers import DefaultRouter
from .api import ApplicationViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register('', ApplicationViewSet, basename='application')

# Define the URL patterns
urlpatterns = router.urls