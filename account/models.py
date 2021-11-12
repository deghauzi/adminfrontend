from decimal import Decimal

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models

from .constants import GENDER_CHOICE, TRANSACTION_TYPE_CHOICES,CONTRIBUTION_TYPES_CHOICES
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=30, unique=True)
    email = models.EmailField(
        db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0


class BankAccountType(models.Model):
    name = models.CharField(max_length=128)
    maximum_withdrawal_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    annual_interest_rate = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        decimal_places=2,
        max_digits=5,
        help_text='Interest rate from 0 - 100'
    )
    interest_calculation_per_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text='The number of times interest will be calculated per year'
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = _('Bank Account Types')

    def __str__(self):
        return self.name

    def calculate_interest(self, principal):
        """
        Calculate interest for each account type.

        This uses a basic interest calculation formula
        """
        p = principal
        r = self.annual_interest_rate
        n = Decimal(self.interest_calculation_per_year)

        # Basic Future Value formula to calculate interest
        interest = (p * (1 + ((r/100) / n))) - p

        return round(interest, 2)

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

# user bank account
class UserBankAccount(models.Model):
    user = models.ForeignKey(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )
    account_type = models.ForeignKey(
        BankAccountType,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    account_no = models.PositiveIntegerField(help_text=(
        'please leave blank it auto generated'
    ), blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    initial_deposit = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    interest_start_date = models.DateField(
        null=True, blank=True,
        help_text=(
            'The month number that interest calculation will start from'
        )
    )
    initial_deposit_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account_no)

    def get_interest_calculation_months(self):
        """
        List of month numbers for which the interest will be calculated

        returns [2, 4, 6, 8, 10, 12] for every 2 months interval
        """
        interval = int(
            12 / self.account_type.interest_calculation_per_year
        )
        start = self.interest_start_date.month
        return [i for i in range(start, 13, interval)]

    def save(self, *args, **kwargs):
        if self.account_type.name == "Gold":
            self.account_no = 3021000 + self.user.id
        if self.account_type.name == "Silver":
            self.account_no = 2021000 + self.user.id + 2
        if self.account_type.name == "Diamond":
            self.account_no = 4021000 + self.user.id + 3
        if self.account_type.name == "Platinum":
            self.account_no = 5021000 + self.user.id + 4
        super(UserBankAccount, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = _('User Bank Account')

# user profile
class UserAddress(models.Model):
    user = models.OneToOneField(
        User,
        related_name='address',
        on_delete=models.CASCADE,
    )
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = _('User Profiles')


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
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
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.account_no}--{self.amount}"

    def save(self, *args, **kwargs):
        if self.transaction_type == 1:
            balance = self.account.initial_deposit + self.amount
            self.balance_after_transaction = balance
        if self.transaction_type == 2:
            balance = self.account.initial_deposit - self.amount
            self.balance_after_transaction = balance
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = _('Transactions')

# bonus account for users
class BonusAccount(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_bonus_acc',
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        UserBankAccount,
        related_name='attached_account',
        on_delete=models.CASCADE,
    )
    bonus_amount_add = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    bonus_amount_withdrawal = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True, blank=True
    )
    total_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    bonus_paid_out  =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('User Bonus Account')
    
    def __str__(self):
        return f"{self.user}: {self.total_amount}"
    
    def save(self, *args,**kwargs):
        if self.bonus_paid_out == True:
            self.total_amount -= self.bonus_amount_withdrawal
        else:
            self.total_amount += self.bonus_amount_add
        super(BonusAccount, self).save(*args,**kwargs)
    
    
    
# Transaction model
class UserTransactions(models.Model):
    user_account = models.ForeignKey(
        UserBankAccount, on_delete=models.CASCADE, related_name='user_account')
    user_account_transactions = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, related_name='user_account_transactions')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_account}"
    class Meta:
        verbose_name_plural = _('User Transactions')


# contribution account
class Contribution(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_contribution_acc',
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        UserBankAccount,
        related_name='user_attached_account',
        on_delete=models.CASCADE,
    )
    contribution_type = models.PositiveSmallIntegerField(choices=CONTRIBUTION_TYPES_CHOICES)
    contribution_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True, blank=True
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account} : {self.contribution_amount}"
    class Meta:
        verbose_name_plural = _('Target Contributions')