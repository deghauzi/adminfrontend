from django.contrib import admin
from .models import (BankAccountType, BankAccount, WalletAccount)
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted

# users account


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("bank_account_no", "user_profile", "bank_account_type",
                    "bank_account_balance", "created_by_admin_user")
    list_filter = ("bank_account_no", "bank_account_type",
                   "created_by_admin_user")
    readonly_fields = ["bank_account_balance",
                       "created_by_admin_user", "bank_account_no", "created"]

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)


# users wallet account
@admin.register(WalletAccount)
class WalletAccountAdmin(admin.ModelAdmin):
    list_display = ("account", "bonus_amount_add",
                    "bonus_amount_withdrawal", "total_amount", "wallet_balance",
                    "bonus_paid_out", "created_by_admin_user")
    list_filter = ("bonus_paid_out", "wallet_balance",
                   "user", "created_by_admin_user")
    readonly_fields = ["total_amount",
                       "created_by_admin_user", "wallet_balance", "account", "user", "created"]

    def save_model(self, request, obj, form, change):
        obj.created_by_admin_user = request.user
        super().save_model(request, obj, form, change)


# account type
@admin.register(BankAccountType)
class BankAccountTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "account_type_image")
    list_filter = ("name", )
    readonly_fields = ["created"]
