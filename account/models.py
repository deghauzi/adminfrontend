from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from safedelete.models import SafeDeleteModel,SOFT_DELETE,NO_DELETE
from safedelete.managers import SafeDeleteManager
from django.utils.translation import gettext_lazy as _
from userprofile.models import User




# bankaccount type model for creating bank account type
class BankAccountType(SafeDeleteModel):
    _safedelete_policy_ = NO_DELETE
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()
    class Meta:
        verbose_name_plural = _('Bank Account Types')

    def __str__(self):
        return self.name

# user bank account
class BankAccount(SafeDeleteModel):
    _safedelete_policy_ = SOFT_DELETE
    user_profile = models.ForeignKey(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    bank_account_type = models.ForeignKey(
        BankAccountType,
        related_name='accounts',
        on_delete=models.SET_NULL,
        null=True
    )
    bank_account_no = models.PositiveIntegerField(help_text=(
        'please leave blank it auto generated'
    ), blank=True)
    bank_account_balance = models.DecimalField(
        help_text=(
            'please leave blank it auto generated'),
        default=0.00,
        max_digits=12,
        decimal_places=2,
        null=True, blank=True
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()

    def __str__(self):
        return str(self.bank_account_no)

    class Meta:
        verbose_name_plural = _('Users Bank Account')



# bonus wallet account for users
class WalletAccount(SafeDeleteModel):
    _safedelete_policy_ = SOFT_DELETE
    user = models.OneToOneField(
        User,
        related_name='user_bonus_acc',
        on_delete=models.CASCADE,
    )
    walletID = models.CharField(max_length=10,default='')
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user_bonus',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    account = models.ForeignKey(
        BankAccount,
        related_name='attached_account',
        on_delete=models.CASCADE,
    )
    wallet_balance = models.DecimalField(
        help_text=(
            'please leave blank it auto generated'),
        default=0.00,
        max_digits=12,
        decimal_places=2,
        null=True, blank=True
    )
    bonus_paid_out = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Users Bonus Account')

    def __str__(self):
        return f"{self.walletID}: {self.wallet_balance}"






# contribution account
