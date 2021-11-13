from .models import UserBankAccount, BonusAccount, Transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=UserBankAccount)
def create_bonus_account(sender, instance, created, **kwargs):
    if created:
        BonusAccount.objects.create(user=instance.user, account=instance,
                                    bonus_amount_add=0.00, total_amount=0.00, bonus_amount_withdrawal=0.00)


@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, created, **kwargs):
    if created:
        try:
            obj, created = UserBankAccount.objects.update_or_create(pk=instance.account.id,
                                                                    defaults={'account_balance': instance.balance_after_transaction})
            print("ID ****")
        except ObjectDoesNotExist:
            print("not valid")

