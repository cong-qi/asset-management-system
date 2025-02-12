from django.contrib import admin
from .models import Asset, AssetHistory


# @admin.register(AssetCategory)
# class AssetCategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)


# @admin.register(AssetType)
# class AssetTypeAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_code",
        "name",
        "brand",
        "model",
        "serial_number",
        "status",
        "owner",
        "parent_asset",
        "updated_at",
    )
    search_fields = ("asset_code", "name", "owner")

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.type == "COMPUTER":
            fields.remove("parent_asset")
        return fields


@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ("asset", "event", "user", "created_at")
    search_fields = ("asset__asset_code", "user")
