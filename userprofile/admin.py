from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User


# @admin.register(UserProfile)
class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    list_display = ("user", "first_name", "last_name",
                    "gender", "created_by_admin_user", "created")
    list_filter = ("user", "last_name",
                   "first_name", "created_by_admin_user")
    fk_name = "created_by_admin_user"

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["user", "first_name", "last_name", "birth_date", "gender", "country", "postal_code", "city",
                    "created_by_admin_user", "created", "profile_img", "street_address"]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            obj = UserProfile.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except UserProfile.DoesNotExist:
            extra_context = extra_context or {}
            extra_context['show_save'] = True
            extra_context['show_save_and_continue'] = True
            extra_context['show_save_and_add_another'] = True

        return super(UserProfileAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)

# Register your models here.


@admin.register(User)
class UserAccountAdmin(UserAdmin):
    list_display = ("email", "username", "is_active", "is_staff", "created")
    list_filter = ("email", "username", "is_active")
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('email', 'username')}),
        ('Permissions', {'fields': ('is_staff',
         "is_active", "groups", "user_permissions")}),
    )
    inlines = (UserProfileAdmin,)
    # ordering=['-created']
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["email", "username", "is_active", "is_staff", "created", "groups", "user_permissions"]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            obj = User.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except User.DoesNotExist:
            extra_context = extra_context or {}
            extra_context['show_save'] = True
            extra_context['show_save_and_continue'] = True
            extra_context['show_save_and_add_another'] = True

        return super(UserAccountAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
