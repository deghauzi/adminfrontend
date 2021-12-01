from django.contrib import admin
from .models import (BankAccountType,BankAccount,WalletAccount)
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted

# users account
class BankAccountAdmin(SafeDeleteAdmin):
   list_display = (highlight_deleted, "highlight_deleted_field", "bank_account_no", "user_profile", "bank_account_type",
                   "bank_account_balance","created_by_admin_user") + SafeDeleteAdmin.list_display
   list_filter = ("bank_account_no", SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
   field_to_highlight = "bank_account_no"
   read_only_fields  = ["bank_account_balance"]
BankAccountAdmin.highlight_deleted_field.short_description = BankAccountAdmin.field_to_highlight
admin.site.register(BankAccount,BankAccountAdmin)

# users wallet account
class WalletAccountAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "highlight_deleted_field", "account", "bonus_amount_add",
                   "bonus_amount_withdrawal","total_amount","wallet_balance","bonus_paid_out","created_by_admin_user") + SafeDeleteAdmin.list_display
    list_filter = ("bonus_paid_out","wallet_balance","user", SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
    field_to_highlight = "account"
WalletAccountAdmin.highlight_deleted_field.short_description = WalletAccountAdmin.field_to_highlight
admin.site.register(WalletAccount,WalletAccountAdmin)

#account type
class BankAccountTypeAdmin(SafeDeleteAdmin):
   list_display = (highlight_deleted, "highlight_deleted_field", "account_type_image") + SafeDeleteAdmin.list_display
#    list_filter = ("name", SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
   field_to_highlight = "name"
BankAccountTypeAdmin.highlight_deleted_field.short_description = BankAccountTypeAdmin.field_to_highlight
admin.site.register(BankAccountType,BankAccountTypeAdmin)