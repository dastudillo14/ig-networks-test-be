from rest_framework.routers import DefaultRouter
from status.api import StatusViewSet

router = DefaultRouter()
router.register('', StatusViewSet, basename='status')

urlpatterns = router.urls