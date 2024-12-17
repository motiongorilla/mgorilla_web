from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Article, Tag, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    # changing how article model looks at the admin panel.
    list_display = ("title", "status", "created_at", "updated_at",)
    list_filter = ("status", "updated_at",)
    search_fields = ("title", "content", "tags",)
    date_hierarchy = "created_at"
    ordering = ("created_at", "updated_at", "tags",)
    readonly_fields = ("created_at", "updated_at",)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide"),
            "fields": ("email", "password1", "password2")
        }),
    )
    list_display = ("email", "username", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email", "username")

admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Tag)
