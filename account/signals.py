from .models import UserBankAccount, BonusAccount
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


@receiver(post_save,sender=UserBankAccount)
def create_bonus_account(sender, instance, created, **kwargs):
    if created:
        BonusAccount.objects.create(user=instance.user,account=instance,bonus_amount_add=0.00,total_amount=0.00,bonus_amount_withdrawal=0.00)
    