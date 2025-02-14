from django.contrib import admin
from .models import Asset, AssetLog
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.fields import Field
from import_export.formats.base_formats import XLSX
from django.utils.text import capfirst
from django.core.exceptions import FieldDoesNotExist


class VerboseNameResource(ModelResource):

    def get_export_headers(self, selected_fields=None):
        headers = []
        for field in selected_fields:
            try:
                headers.append(
                    capfirst(self.Meta.model._meta.get_field(field).verbose_name)
                )
            except FieldDoesNotExist:
                headers.append(field.column_name)

        return headers


class AssetResource(VerboseNameResource):

    class Meta:
        model = Asset
        fields = (
            "id",
            "asset_code",
            "name",
            "type",
            "brand",
            "model",
            "serial_number",
            "category",
            "price",
            "purchase_date",
            "status",
            "owner",
            "location",
        )
        export_order = fields


# @admin.register(AssetCategory)
# class AssetCategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)


# @admin.register(AssetType)
# class AssetTypeAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)


@admin.register(Asset)
class AssetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "asset_code",
        "name",
        "type",
        "brand",
        "model",
        "serial_number",
        "category",
        "price",
        "purchase_date",
        "status",
        "owner",
        "location",
        "updated_at",
    )

    list_filter = ("category", "status", "type")
    search_fields = ("asset_code", "name", "owner")
    resource_class = AssetResource

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     if not change:
    #         AssetLog.objects.create(
    #             asset=obj,
    #             event="CREATE",
    #             from_user=None,
    #             to_user=obj.owner,
    #             from_department=None,
    #             to_department=obj.department,
    #             description="资产入库",
    #         )

    def get_export_formats(self):
        formats = [XLSX]
        return formats


@admin.register(AssetLog)
class AssetLogAdmin(admin.ModelAdmin):
    list_display = (
        "asset",
        "event",
        # "from_user",
        # "to_user",
        # "from_department",
        # "to_department",
        "operator",
        "operated_at",
        "remark",
    )
    list_filter = ("event",)
    search_fields = ("asset__asset_code", "operator")
