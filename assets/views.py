from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Asset, AssetLog
from .serializers import AssetSerializer, AssetLogSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def perform_update(self, serializer):
        return serializer.save()


class AssetLogViewSet(viewsets.ModelViewSet):
    queryset = AssetLog.objects.all()
    serializer_class = AssetLogSerializer
