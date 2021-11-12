from django.contrib import admin

from .models import (User,BankAccountType,UserAddress,UserBankAccount,
                     Transaction,BonusAccount,Contribution)

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)
admin.site.register(BankAccountType)
admin.site.register(Transaction)
admin.site.register(BonusAccount)
admin.site.register(Contribution)
