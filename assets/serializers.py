from rest_framework import serializers
from .models import Asset, AssetHistory


class AssetHistorySerializer(serializers.ModelSerializer):
    event_display = serializers.SerializerMethodField()

    class Meta:
        model = AssetHistory
        fields = [
            "id",
            "event",
            "event_display",
            "user",
            "location",
            "reason",
            "created_at",
        ]

    def get_event_display(self, obj):
        return obj.get_event_display()


class AssetSerializer(serializers.ModelSerializer):
    history = AssetHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Asset
        fields = "__all__"
