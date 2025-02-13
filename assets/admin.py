from django.contrib import admin
from .models import Asset, AssetHistory
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

    # id = Field(attribute="id", column_name="主键")
    # asset_code = Field(attribute="asset_code", column_name="资产编号")
    # name = Field(attribute="name", column_name="资产名称")
    # category = Field(attribute="category", column_name="资产分类")

    # type = Field(attribute="type", column_name="类型")

    # brand = Field(attribute="brand", column_name="品牌")
    # model = Field(attribute="model", column_name="型号")
    # serial_number = Field(attribute="serial_number", column_name="序列号")
    # price = Field(attribute="price", column_name="购置价格")
    # purchase_date = Field(attribute="purchase_date", column_name="购置日期")

    # status = Field(attribute="status", column_name="状态")
    # model = Field(attribute="model", column_name="型号")
    # owner = Field(attribute="owner", column_name="当前领用人")
    # location = Field(attribute="location", column_name="存放位置")
    # parent_asset = Field(attribute="parent_asset", column_name="赠品来源")

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
            "parent_asset",
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
        "parent_asset",
        "updated_at",
    )

    list_filter = ("category", "status", "type")
    search_fields = ("asset_code", "name", "owner")
    resource_class = AssetResource

    def get_export_formats(self):
        formats = [XLSX]
        return formats

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.type == "COMPUTER":
            fields.remove("parent_asset")
        return fields


@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ("asset", "event", "operator", "operated_at")
    search_fields = ("asset__asset_code", "user")
