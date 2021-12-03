from django.contrib import admin
from .models import TargetContribution, DailyContribution


@admin.register(DailyContribution)
class DailyContributionAdmin(admin.ModelAdmin):
    list_display = ("account", "amount", "balance_after_transaction",
                    "transaction_type", "created_by_admin_user")
    list_filter = ("account", "amount",
                   "created_by_admin_user", "transaction_type")
    readonly_fields = ["balance_after_transaction",
                       "created_by_admin_user", "created"]

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)
        
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["account", "amount"]
    #     else:
    #         return []


@admin.register(TargetContribution)
class TargetContributionAdmin(admin.ModelAdmin):
    list_display = ("account", "contribution_amount", "user", "contribution_type",
                    "transaction_type", "created_by_admin_user")
    list_filter = ("account", "contribution_amount",
                   "created_by_admin_user", "transaction_type")
    readonly_fields = ["contribution_balance", "user",
                       "created_by_admin_user", "created"]

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)
