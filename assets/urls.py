from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, AssetLogViewSet

router = DefaultRouter()
router.register(r"assets", AssetViewSet, basename="assets")
router.register(r"asset-log", AssetLogViewSet, basename="asset-log")

urlpatterns = router.urls
