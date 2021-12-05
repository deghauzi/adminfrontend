from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("email", "username", "is_active", "is_staff", "created")
    list_filter = ("email", "username", "is_active")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', "is_active","groups","user_permissions")}),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name","last_name",
                    "gender", "created_by_admin_user", "created")
    list_filter = ("user", "last_name",
                   "first_name", "created_by_admin_user")
    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)

# Register your models here.
