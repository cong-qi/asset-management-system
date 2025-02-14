from django.db import models
from accounts.models import User, Department

# class AssetCategory(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name


class AssetType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="资产类型")

    def __str__(self):
        return self.name


class Asset(models.Model):
    TYPE_CHOICES = (
        ("COMPUTER", "计算设备"),
        ("CAMERA", "相机"),
        ("LENS", "镜头"),
        ("MONITOR", "显示器"),
        ("KEYBOARD", "键盘"),
        ("MOUSE", "鼠标"),
    )

    CATEGORY_CHOICES = (
        ("FIXED", "固定资产"),
        ("CONSUMABLE", "低值易耗品"),
    )

    STATUS_CHOICES = (
        ("IN_STOCK", "在库"),
        ("ALLOCATED", "已领用"),
        ("MAINTENANCE", "维修"),
        ("SCRAPPED", "已报废"),
    )

    asset_code = models.CharField(
        max_length=50, unique=True, blank=True, null=True, verbose_name="资产编号"
    )
    name = models.CharField(max_length=100, verbose_name="资产名称")
    type = models.ForeignKey(
        AssetType,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="资产类型",
    )
    # type = models.CharField(
    #     max_length=100,
    #     choices=TYPE_CHOICES,
    #     verbose_name="资产类型",
    #     blank=True,
    #     null=True,
    # )
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name="品牌")
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name="型号")
    serial_number = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name="序列号"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True,
        verbose_name="资产分类",
    )

    purchase_date = models.DateField(verbose_name="购置日期")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="购置价格"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="IN_STOCK",
        verbose_name="资产状态",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="owned_assets",
        verbose_name="当前领用人",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="department_assets",
        verbose_name="当前所属部门",
    )
    location = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="存放位置"
    )

    # parent_asset = models.ForeignKey(
    #     "self",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="gift_assets",
    #     verbose_name="赠品来源",
    # )
    # vendor = models.CharField(
    #     max_length=100, blank=True, null=True, verbose_name="供应商"
    # )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def save(self, *args, **kwargs):

        if self.price and self.price >= 5000:
            self.category = "FIXED"
        else:
            self.category = "CONSUMABLE"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset_code} - {self.name}"


class AssetLog(models.Model):
    EVENT_CHOICES = (
        ("CREATE", "录入"),
        ("PURCHASE", "购置"),
        ("TRANSFER", "调拨"),
        ("ALLOCATE", "领用"),
        ("RETURN", "归还"),
        ("REPAIR", "维修"),
        ("SCRAP", "报废"),
        ("UPDATE", "更新"),
        ("DELETE", "删除"),
    )

    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name="history", verbose_name="关联资产"
    )
    event = models.CharField(
        max_length=20, choices=EVENT_CHOICES, verbose_name="变更事件"
    )
    # from_user = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="assethistory_from",
    #     verbose_name="原领用人",
    # )
    # to_user = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="assethisstory_to",
    #     verbose_name="新领用人",
    # )
    # from_department = models.ForeignKey(
    #     Department,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="assethisstory_from_dep",
    #     verbose_name="原部门",
    # )
    # to_department = models.ForeignKey(
    #     Department,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="assethisstory_to_dep",
    #     verbose_name="新部门",
    # )
    # previous_status = models.CharField(
    #     max_length=20, choices=Asset.STATUS_CHOICES, verbose_name="原状态"
    # )
    # new_status = models.CharField(
    #     max_length=20, choices=Asset.STATUS_CHOICES, verbose_name="新状态"
    # )
    # previous_owner = models.CharField(
    #     max_length=50, blank=True, null=True, verbose_name="原领用人"
    # )
    # new_owner = models.CharField(
    #     max_length=50, blank=True, null=True, verbose_name="新领用人"
    # )
    # previous_location = models.CharField(
    #     max_length=100, blank=True, null=True, verbose_name="原存放位置"
    # )
    # new_location = models.CharField(
    #     max_length=100, blank=True, null=True, verbose_name="新存放位置"
    # )
    # previous_price = models.DecimalField(
    #     max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="原价格"
    # )

    # new_price = models.DecimalField(
    #     max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="新价格"
    # )

    operator = models.CharField(max_length=50, verbose_name="操作人")

    remark = models.TextField(blank=True, null=True, verbose_name="备注")
    operated_at = models.DateTimeField(auto_now_add=True, verbose_name="操作时间")

    def __str__(self):
        return f"{self.asset.asset_code} - {self.event} on {self.operated_at}"


# class ComputerDetails(models.Model):
#     asset = models.OneToOneField(
#         Asset, on_delete=models.CASCADE, related_name="computer_details"
#     )
#     cpu = models.CharField(max_length=100, blank=True, null=True, verbose_name="CPU")
#     ram = models.CharField(max_length=100, blank=True, null=True, verbose_name="内存")
#     storage = models.CharField(
#         max_length=100, blank=True, null=True, verbose_name="存储"
#     )
#     gpu = models.CharField(max_length=100, blank=True, null=True, verbose_name="显卡")

#     def __str__(self):
#         return f"{self.asset.asset_code} - {self.cpu}, {self.ram}, {self.storage}"


# class PeripheralDetails(models.Model):
#     asset = models.OneToOneField(
#         Asset, on_delete=models.CASCADE, related_name="peripheral_details"
#     )
