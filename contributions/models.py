from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel,SOFT_DELETE
from safedelete.managers import  SafeDeleteManager
from utils.constants import  TRANSACTION_TYPE_CHOICES, CONTRIBUTION_TYPES_CHOICES
from account.models import BankAccount,WalletAccount
from userprofile.models import User


# user daily monthly contributions
class DailyContribution(SafeDeleteModel):
    _safedelet_policy_ = SOFT_DELETE
    account = models.ForeignKey(
        BankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user_transactions',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        help_text=(
            'please leave blank it auto generated'
        ), blank=True, null=True
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    TransID = models.CharField(max_length=12,default='')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()

    def __str__(self):
        return f"{self.account.bank_account_no}:{self.amount}"
class WalletTransaction(SafeDeleteModel):
    _safedelet_policy_ = SOFT_DELETE
    bank_account_user = models.ForeignKey(
        BankAccount,
        related_name='bank_account_user',
        on_delete=models.CASCADE,
        default=''
    )
    wallet_account = models.ForeignKey(
        WalletAccount,
        related_name='wallet_transactions',
        on_delete=models.CASCADE,
    )
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user_wallet_transactions',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        help_text=(
            'please leave blank it auto generated'
        ), blank=True, null=True
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    TransID = models.CharField(max_length=12,default='')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()

    def __str__(self):
        return f"{self.wallet_account.walletID}:{self.amount}"



    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Wallet Transactions')

#targeted contributions for salah and mortage
class TargetContribution(SafeDeleteModel):
    created_by_admin_user = models.ForeignKey(
        User,
        related_name='created_by_admin_user_target',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    account = models.ForeignKey(
        BankAccount,
        related_name='user_attached_account',
        on_delete=models.SET_NULL,null=True
    )
    contribution_type = models.PositiveSmallIntegerField(
        choices=CONTRIBUTION_TYPES_CHOICES)
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES,null=True, blank=True)
    contribution_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True, blank=True
    )
    contribution_balance = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True, blank=True,default='0'
    )
    TransID = models.CharField(max_length=12,default='')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = SafeDeleteManager()

    def __str__(self):
        return f"{self.account} : {self.contribution_amount}"

    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Target Contributions')


    # def calculate_interest(self, principal):
    #     """
    #     Calculate interest for each account type.

    #     This uses a basic interest calculation formula
    #     """
    #     p = principal
    #     r = self.annual_interest_rate
    #     n = Decimal(self.interest_calculation_per_year)

    #     # Basic Future Value formula to calculate interest
    #     interest = (p * (1 + ((r/100) / n))) - p

    #     return round(interest, 2)
    
    
    
    # def increment_invoice_number():
#     last_invoice = Invoice.objects.all().order_by('id').last()
#     if not last_invoice:
#          return 'MAG0001'
#     invoice_no = last_invoice.invoice_no
#     invoice_int = int(invoice_no.split('MAG')[-1])
#     new_invoice_int = invoice_int + 1
#     new_invoice_no = 'MAG' + str(new_invoice_int)
#     return new_invoice_no

# Now use this function as default value in your model filed.

# invoice_no = models.CharField(max_length=500, default=increment_invoice_number, null=True, blank=True)

