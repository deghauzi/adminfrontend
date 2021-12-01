from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel,SOFT_DELETE
from safedelete.managers import  SafeDeleteManager
from utils.constants import  TRANSACTION_TYPE_CHOICES, CONTRIBUTION_TYPES_CHOICES
from account.models import BankAccount
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
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()

    def __str__(self):
        return f"{self.account.bank_account_no}:{self.amount}"

    def save(self, *args, **kwargs):
        if self.transaction_type == 1:
            balance = self.account.bank_account_balance + self.amount
            if self.account.bank_account_balance != 0:
                self.balance_after_transaction = balance
            else:
                self.balance_after_transaction = balance
                self.account.bank_account_balance = balance
        if self.transaction_type == 2:
            if self.account.bank_account_balance == 0:
                raise ValidationError('not allowed')
            else:
                withdrawal_balance = self.account.bank_account_balance - self.amount
                self.balance_after_transaction = withdrawal_balance
                self.account.bank_bank_account_balance = withdrawal_balance
        super(DailyContribution, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Daily Contributions')

#targeted contributions for salah and mortage
class TargetContribution(SafeDeleteModel):
    user = models.ForeignKey(
        User,
        related_name='user_contribution_acc',
        on_delete=models.CASCADE,
    )
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
        null=True, blank=True
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = SafeDeleteManager()

    def __str__(self):
        return f"{self.account} : {self.contribution_amount}"

    class Meta:
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

