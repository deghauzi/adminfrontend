from .models import BankAccount, WalletAccount
from contributions.models import DailyContribution
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=BankAccount)
def create_bonus_account(sender, instance, created, **kwargs):
    if created:
        WalletAccount.objects.create(user=instance.user_profile, account=instance,wallet_balance=0.00,
            bonus_amount_add=0.00, total_amount=0.00, bonus_amount_withdrawal=0.00)


@receiver(post_save, sender=DailyContribution)
def update_account_balance(sender, instance, created, **kwargs):
    if created:
        try:
            obj, created = BankAccount.objects.update_or_create(pk=instance.account.id,
                                                                    defaults={'bank_account_balance': instance.balance_after_transaction})
        except ObjectDoesNotExist:
            print("not valid")

