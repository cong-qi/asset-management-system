from django.contrib import admin
from .models import Asset, AssetCategory, AssetType, AssetHistory


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_code",
        "serial_number",
        "name",
        "status",
        "owner",
        "updated_at",
    )
    search_fields = ("asset_code", "name", "owner")


@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ("asset", "event", "user", "created_at")
    search_fields = ("asset__asset_code", "user")
