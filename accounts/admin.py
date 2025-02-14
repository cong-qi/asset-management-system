from django.contrib import admin
from .models import User, Department


# 注册 Department 模型
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "wechat_department_id")  # 显示字段
    search_fields = ("name",)  # 可搜索字段


# 注册 User 模型
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "department", "job_title", "is_active")
    list_filter = ("is_active", "department")  # 可筛选字段
    search_fields = ("username", "full_name", "email")
