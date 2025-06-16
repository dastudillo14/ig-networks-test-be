from rest_framework.routers import DefaultRouter
from .api import JobPostViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register('', JobPostViewSet, basename='jobpost')

# Define the URL patterns
urlpatterns = router.urls