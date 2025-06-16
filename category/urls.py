from rest_framework.routers import DefaultRouter
from category.api import CategoryViewSet

router = DefaultRouter()
router.register('', CategoryViewSet, basename='category')

urlpatterns = router.urls