from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User
import csv
from django.http import HttpResponse
from .form  import  UserChangeForm, UserCreationForm


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        "user",
        "first_name",
        "last_name",
        "gender",
        "created_by_admin_user",
        "created",
    )
    list_filter = ("user", "last_name", "first_name", "created_by_admin_user")
    fk_name = "created_by_admin_user"

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "user",
                "created_by_admin_user",
                "created",
            ]
        else:
            return ["created_by_admin_user","created"]

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = UserProfile.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except UserProfile.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(UserProfileAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def has_add_permission(self, request, obj=None):
        return True
    
    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)


# Register your models here.


class UserAccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ("email", "username", "is_active", "is_admin","created")
    list_filter = ("email", "username", "is_active")
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        ("Personal info", {"fields": ("username",)}),
        (
            "Permissions",
            {"fields": ("is_admin", "is_active","groups")},
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',"is_admin", "is_active", "groups"),
        }),
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "email",
                "is_admin",
                "created"
            ]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = User.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except User.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(UserAccountAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )
        
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def has_add_permission(self, request, obj=None):
        return True
    
admin.site.register(User, UserAccountAdmin)
