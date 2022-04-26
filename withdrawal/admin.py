import csv
from django.contrib import admin
from .models import WithdrawalRequest
from utils.functions import  gen_key
from django.http import HttpResponse


@admin.register(WithdrawalRequest)
class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ("request_user_account", "request_from_account","TransID", "request_amount",
                    "request_expected_date", "request_proccessed", "request_proccessed_by")
    list_filter = ("request_amount", "request_from_account",
                   "request_expected_date", "request_proccessed", "request_proccessed_by")
    readonly_fields = ["TransID","request_user","request_amount","request_reasons","request_proccessed_by",
                       "request_expected_date", "request_from_account", "request_user_account"]

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = WithdrawalRequest.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except WithdrawalRequest.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(WithdrawalRequestAdmin, self).changeform_view(
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
        obj.request_proccessed_by =request.user
        obj.TransID=f"wth_{gen_key(5)}"
        return super().save_model(request, obj, form, change)
