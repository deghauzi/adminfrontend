from django.contrib import admin
from .models import TargetContribution, DailyContribution, WalletTransaction
import csv
from django.http import HttpResponse
from .form import DailyContributionForm, WalletTransactionForm
from utils.functions import gen_key_wa


@admin.register(DailyContribution)
class DailyContributionAdmin(admin.ModelAdmin):
    form = DailyContributionForm
    list_display = (
        "TransID",
        "bank_account",
        "amount",
        "approved",
        "balance_after_transaction",
        "transaction_type",
        "created_by_admin_user",
    )
    list_filter = (
        "bank_account",
        "amount",
        "approved",
        "created_by_admin_user",
        "transaction_type",
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "TransID",
                "transaction_type",
                "bank_account",
                "user_account",
                "amount",
                "balance_after_transaction",
                "created_by_admin_user",
                "created",
            ]
        else:
            return ["TransID","balance_after_transaction",
                "created_by_admin_user"]

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = DailyContribution.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except DailyContribution.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(DailyContributionAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.transaction_type == 1 and obj.bank_account.bank_account_balance == 0:
            obj.balance_after_transaction = obj.amount
        if obj.transaction_type == 1 and obj.bank_account.bank_account_balance > 0:
            balance = obj.bank_account.bank_account_balance + obj.amount
            obj.balance_after_transaction = balance
        if obj.transaction_type == 2:
            obj.balance_after_transaction = (
                obj.bank_account.bank_account_balance - obj.amount
            )
        obj.TransID = f"{gen_key_wa(5)}"
        obj.user_account = obj.bank_account.user_profile
        super().save_model(request, obj, form, change)


@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    form = WalletTransactionForm
    list_display = (
        "TransID",
        "bank_account_user",
        "amount",
        "approved",
        "balance_after_transaction",
        "transaction_type",
        "created_by_admin_user",
    )
    list_filter = (
        "bank_account_user",
        "amount",
        "approved",
        "created_by_admin_user",
        "transaction_type",
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "TransID",
                "transaction_type",
                "bank_account_user",
                "amount",
                "balance_after_transaction",
                "created_by_admin_user",
                "created",
                
            ]
        else:
            return ["TransID","balance_after_transaction","created_by_admin_user",
                "created"]

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = WalletTransaction.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except WalletTransaction.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(WalletTransactionAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"

    def has_add_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.transaction_type == 1 and obj.wallet_account.wallet_balance == 0:
            obj.balance_after_transaction = obj.amount
        if obj.transaction_type == 1 and obj.wallet_account.wallet_balance > 0:
            balance = obj.wallet_account.wallet_balance + obj.amount
            obj.balance_after_transaction = balance
        if obj.transaction_type == 2:
            obj.balance_after_transaction = (
                obj.wallet_account.wallet_balance - obj.amount
            )
        obj.TransID = f"{gen_key_wa(5)}"
        super().save_model(request, obj, form, change)


@admin.register(TargetContribution)
class TargetContributionAdmin(admin.ModelAdmin):
    list_display = (
        "TransID",
        "user_account",
        "contribution_amount",
        "contribution_type",
        "transaction_type",
        "approved",
        "created_by_admin_user",
    )
    list_filter = (
        "user_account",
        "contribution_amount",
        "approved",
        "created_by_admin_user",
        "transaction_type",
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "TransID",
        "user_account",
        "contribution_amount",
        "contribution_balance",
        "contribution_type",
        "transaction_type",
        "created_by_admin_user",
         "created"  
            ]
        else:
            return [
                "TransID",
        "contribution_balance",
        "created_by_admin_user",
        "created"
                
            ]
        
        
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        try:
            obj = TargetContribution.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context["show_save"] = True
                extra_context["show_save_and_continue"] = False
                extra_context["show_save_and_add_another"] = False
                extra_context["show_delete_link"] = False
        except TargetContribution.DoesNotExist:
            extra_context = extra_context or {}
            extra_context["show_save"] = True
            extra_context["show_save_and_continue"] = True
            extra_context["show_save_and_add_another"] = True

        return super(TargetContributionAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.transaction_type == 1 and obj.contribution_balance == 0.00:
            obj.contribution_balance = obj.contribution_amount
        if obj.transaction_type == 1 and int(obj.contribution_balance) > 0:
            balance = obj.contribution_balance + obj.contribution_amount
            obj.contribution_balance = balance
        if obj.transaction_type == 2:
            pass
            # obj.contribution_balance = obj.contribution_amount
        obj.TransID = f"{gen_key_wa(5)}"
        super().save_model(request, obj, form, change)

