from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class WithdrawalRequest(models.Model):
    request_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,null=True,related_name="request_withdrawal")
    request_amount = models.DecimalField(decimal_places=2,
        max_digits=12)
    request_reasons = models.TextField(help_text="reason for withdrawal")
    request_date = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('Withdrawal Request')

    def __str__(self):
        return f"{self.request_user.username}: {self.request_amount}"