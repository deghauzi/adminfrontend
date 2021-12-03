from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from account.models import BankAccount
from utils.constants import REQUEST_FROM_ACCOUNT


class WithdrawalRequest(models.Model):
    request_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL, null=True, related_name="request_withdrawal")
    request_proccessed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                        on_delete=models.SET_NULL, null=True, blank=True,
                        related_name="request_proccessed_by")
    request_user_account = models.ForeignKey(BankAccount,
                    on_delete=models.SET_NULL,blank=True,null=True,related_name="request_withdrawal_acc")
    request_amount = models.DecimalField(decimal_places=2,
                                         max_digits=12)
    request_reasons = models.TextField(help_text="reason for withdrawal")
    request_expected_date = models.CharField(max_length=12)
    request_proccessed = models.BooleanField(default=False)
    request_from_account = models.CharField(
        max_length=20, choices=REQUEST_FROM_ACCOUNT)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Withdrawal Request')

    def __str__(self):
        return f"{self.request_user.username}: {self.request_amount}"
