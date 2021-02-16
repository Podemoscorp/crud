from django.contrib import admin
from user.models import User, Role


class AdminUser(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "date_joined",
        "cpf",
        "role",
        "phone_number",
    )
    list_display_links = (
        "id",
        "first_name",
        "last_name",
        "email",
        "date_joined",
        "cpf",
        "role",
        "phone_number",
    )
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "email",
        "date_joined",
        "cpf",
        "role",
        "address",
        "phone_number",
        "description",
    )
    list_per_page = 20


class AdminRole(admin.ModelAdmin):
    list_display = ("id", "name", "value", "created")
    list_display_links = ("id", "name", "value", "created")
    search_fields = ("id", "name", "value", "created")
    list_per_page = 20


admin.site.register(User, AdminUser)
admin.site.register(Role, AdminRole)
