from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Asset, AssetLog


# 当资产对象被创建或更新时，自动记录日志
@receiver(pre_save, sender=Asset)
def log_asset_change(sender, instance: Asset, **kwargs):
    # 如果是创建资产时
    if not instance.pk:
        AssetLog.objects.create(
            asset=instance,
            event="CREATE",  # 记录为“创建”事件
            # from_user=None,  # 无从属用户（资产初始时没有）
            # to_user=instance.owner,
            # from_department=None,  # 无从属部门
            # to_department=instance.department,
            operator="system",
            remark="资产入库",
        )
    else:
        # 如果是更新资产时
        old_instance = Asset.objects.get(pk=instance.pk)
        if old_instance:

            changed_fields = []
            for field in instance._meta.fields:
                field_name = field.name
                old_value = getattr(old_instance, field_name)
                new_value = getattr(instance, field_name)
                # 如果值发生变化,记录字段变化
                print("old: ", old_value)
                print("new: ", new_value)
                if old_value != new_value:
                    changed_fields.append(
                        f"{field.verbose_name}: 从 '{old_value}' 更新为 '{new_value}'"
                    )

        if changed_fields:
            remark = "\n".join(changed_fields)

            AssetLog.objects.create(
                asset=instance,
                event="UPDATE",  # 记录为“更新”事件
                # from_user=None,  # 无从属用户
                # to_user=instance.current_owner,
                # from_department=None,  # 无从属部门
                # to_department=instance.current_department,
                operator="system",
                remark=remark,
            )


# # 当资产被删除时，记录删除日志
# @receiver(post_delete, sender=Asset)
# def log_asset_deletion(sender, instance, **kwargs):
#     AssetLog.objects.create(
#         asset=instance,
#         event="DELETE",  # 记录为“删除”事件
#         # from_user=None,  # 无从属用户
#         # to_user=None,  # 无目标用户
#         # from_department=None,  # 无从属部门
#         # to_department=None,  # 无目标部门
#         remark="资产已删除",
#     )
