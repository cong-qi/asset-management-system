from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Asset, AssetHistory
from .serializers import AssetSerializer, AssetHistorySerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def perform_update(self, serializer):
        return serializer.save()


class AssetHistoryViewSet(viewsets.ModelViewSet):
    queryset = AssetHistory.objects.all()
    serializer_class = AssetHistorySerializer
