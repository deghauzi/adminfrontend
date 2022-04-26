from .models import BankAccount, WalletAccount
from contributions.models import DailyContribution, WalletTransaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from utils.functions import  gen_key_wa

@receiver(post_save, sender=BankAccount)
def create_bonus_account(sender, instance, created, **kwargs):
    if created:
        WalletAccount.objects.create(user=instance.user_profile,walletID=f"{gen_key_wa(7)}",
                                     account=instance,wallet_balance=0.00,
                                     created_by_admin_user=instance.created_by_admin_user)


@receiver(post_save, sender=DailyContribution)
def update_account_balance(sender, instance, created, **kwargs):
    if created:
        try:
            obj, created = BankAccount.objects.update_or_create(pk=instance.bank_account.id,
                            defaults={'bank_account_balance': instance.balance_after_transaction})
        except ObjectDoesNotExist:
            print('not working')
            
            
            
@receiver(post_save, sender=WalletTransaction)
def update_wallet_balance(sender, instance, created, **kwargs):
    if created:
        try:
            obj, created = WalletAccount.objects.update_or_create(pk=instance.wallet_account.id,
                defaults={'wallet_balance': instance.balance_after_transaction})
        except ObjectDoesNotExist:
            print('not working')

