from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, AssetHistoryViewSet

router = DefaultRouter()
router.register(r"assets", AssetViewSet, basename="assets")
router.register(r"asset-history", AssetHistoryViewSet, basename="asset-history")

urlpatterns = router.urls
