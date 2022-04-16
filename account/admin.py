from django.contrib import admin
from .models import (BankAccountType, BankAccount, WalletAccount)
from utils.functions import  gen_key, gen_key_wa
import csv
from django.http import HttpResponse

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
            return ["created_by_admin_user","bank_account_no","bank_account_balance"]

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
    list_display = ("walletID", "wallet_balance",
                    "bonus_paid_out", "created_by_admin_user")
    list_filter = ("bonus_paid_out", "wallet_balance",
                   "user", "created_by_admin_user")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["account", "wallet_balance",
                    "bonus_paid_out", "created_by_admin_user"]
        else:
            return ["walletID","wallet_balance","created_by_admin_user"]
        
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
