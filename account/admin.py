from django.contrib import admin
from .models import (BankAccountType, BankAccount, WalletAccount)


# users account


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank_account_no", "user_profile", "bank_account_type",
                    "bank_account_balance", "created_by_admin_user")
    list_filter = ("bank_account_no", "bank_account_type",
                   "created_by_admin_user")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["bank_account_no", "user_profile", "bank_account_type",
                    "bank_account_balance", "created_by_admin_user", "created"]
        else:
            return []

    def changeform_view(self, request, object_id=None,form_url='', extra_context=None):
        try:
            obj = BankAccount.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except BankAccount.DoesNotExist:
            extra_context = extra_context or {}
            extra_context['show_save'] = True
            extra_context['show_save_and_continue'] = True
            extra_context['show_save_and_add_another'] = True

        return super(BankAccountAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.bank_account_type.name == "Gold":
            obj.bank_account_no = 3021000 + obj.user_profile.id
        if obj.bank_account_type.name == "Silver":
            obj.bank_account_no = 2021000 + obj.user_profile.id + 2
        if obj.bank_account_type.name == "Diamond":
            obj.bank_account_no = 4021000 + obj.user_profile.id + 3
        if obj.bank_account_type.name == "Platinum":
            obj.bank_account_no = 5021000 + obj.user_profile.id + 4
        super().save_model(request, obj, form, change)


# users wallet account
@admin.register(WalletAccount)
class WalletAccountAdmin(admin.ModelAdmin):
    list_display = ("account", "bonus_amount_add",
                    "bonus_amount_withdrawal", "total_amount", "wallet_balance",
                    "bonus_paid_out", "created_by_admin_user")
    list_filter = ("bonus_paid_out", "wallet_balance",
                   "user", "created_by_admin_user")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["account", "bonus_amount_add",
                    "bonus_amount_withdrawal", "total_amount", "wallet_balance",
                    "bonus_paid_out", "created_by_admin_user"]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            obj = WalletAccount.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except WalletAccount.DoesNotExist:
            extra_context = extra_context or {}
            extra_context['show_save'] = True
            extra_context['show_save_and_continue'] = True
            extra_context['show_save_and_add_another'] = True

        return super(WalletAccountAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        if obj.bonus_paid_out == True:
            obj.total_amount -= obj.bonus_amount_withdrawal
        else:
            obj.total_amount += obj.bonus_amount_add
        super().save_model(request, obj, form, change)


# account type
@admin.register(BankAccountType)
class BankAccountTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "account_type_image")
    list_filter = ("name", )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name", "account_type_image", "created"]
        else:
            return []

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            obj = BankAccountType.objects.get(pk=object_id)
            if obj:
                extra_context = extra_context or {}
                extra_context['show_save'] = False
                extra_context['show_save_and_continue'] = False
                extra_context['show_save_and_add_another'] = False
                extra_context['show_delete_link'] = False
        except BankAccountType.DoesNotExist:
            extra_context = extra_context or {}
            extra_context['show_save'] = True
            extra_context['show_save_and_continue'] = True
            extra_context['show_save_and_add_another'] = True

        return super(BankAccountTypeAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
