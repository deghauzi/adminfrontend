from django.contrib import admin
from .models import WithdrawalRequest


@admin.register(WithdrawalRequest)
class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ("request_user_account", "request_from_account", "request_amount",
                    "request_expected_date", "request_proccessed", "request_proccessed_by")
    list_filter = ("request_amount", "request_from_account",
                   "request_expected_date", "request_proccessed", "request_proccessed_by")
    readonly_fields = ["request_user","request_amount","request_reasons","request_proccessed_by",
                       "request_expected_date", "request_from_account", "request_user_account"]
    def save_model(self, request, obj, form, change):
        obj.request_proccessed_by =request.user
        return super().save_model(request, obj, form, change)
