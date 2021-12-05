from django.contrib import admin,messages
from .models import TargetContribution, DailyContribution
from django.core.exceptions import ValidationError
from .form import DailyContributionForm
@admin.register(DailyContribution)
class DailyContributionAdmin(admin.ModelAdmin):
    form = DailyContributionForm
    list_display = ("account", "amount", "balance_after_transaction",
                    "transaction_type", "created_by_admin_user")
    list_filter = ("account", "amount",
                   "created_by_admin_user", "transaction_type")
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["transaction_type","account", "amount", "balance_after_transaction",
                                       "created_by_admin_user", "created"]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            obj = DailyContribution.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except DailyContribution.DoesNotExist:
                extra_context = extra_context or {}
                extra_context['show_save'] = True
                extra_context['show_save_and_continue'] = True
                extra_context['show_save_and_add_another'] = True
            
        return super(DailyContributionAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
    # def has_add_permission(self, request, obj=None):
    #     return False
    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.transaction_type == 1 and obj.account.bank_account_balance == 0:
            obj.balance_after_transaction = obj.amount
        if obj.transaction_type == 1 and obj.account.bank_account_balance > 0:
            balance = obj.account.bank_account_balance + obj.amount
            obj.balance_after_transaction = balance
        if obj.transaction_type == 2:
            obj.balance_after_transaction = obj.account.bank_account_balance - obj.amount
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
