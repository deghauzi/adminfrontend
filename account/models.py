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
    account_type_image = models.ImageField(_("Image Logo"),
                                           help_text='logo image for the type of account')
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
        default=0,
        max_digits=12,
        decimal_places=2,
        null=True, blank=True
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    objects = SafeDeleteManager()

    def __str__(self):
        return str(self.bank_account_no)

    def save(self, *args, **kwargs):
        if self.bank_account_type.name == "Gold":
            self.bank_account_no = 3021000 + self.user_profile.id
        if self.bank_account_type.name == "Silver":
            self.bank_account_no = 2021000 + self.user_profile.id + 2
        if self.bank_account_type.name == "Diamond":
            self.bank_account_no = 4021000 + self.user_profile.id + 3
        if self.bank_account_type.name == "Platinum":
            self.bank_account_no = 5021000 + self.user_profile.id + 4
        super(BankAccount, self).save(*args, **kwargs)

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
    wallet_balance = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    bonus_paid_out = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('User Bonus Account')

    def __str__(self):
        return f"{self.user}: {self.total_amount}"

    def save(self, *args, **kwargs):
        if self.bonus_paid_out == True:
            self.total_amount -= self.bonus_amount_withdrawal
        else:
            self.total_amount += self.bonus_amount_add
        super(WalletAccount, self).save(*args, **kwargs)





# contribution account
