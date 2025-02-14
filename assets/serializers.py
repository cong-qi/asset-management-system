from rest_framework import serializers
from .models import Asset, AssetLog


class AssetLogSerializer(serializers.ModelSerializer):
    event_display = serializers.SerializerMethodField()

    class Meta:
        model = AssetLog
        fields = "__all__"

    def get_event_display(self, obj):
        return obj.get_event_display()


class AssetSerializer(serializers.ModelSerializer):
    history = AssetLogSerializer(many=True, read_only=True)

    class Meta:
        model = Asset
        fields = "__all__"
