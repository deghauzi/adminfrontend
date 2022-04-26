from rest_framework import serializers

from account.models import WalletAccount
from .models import DailyContribution, TargetContribution
from account.account_serializers import BankAccountOnlySerializer


# daily contribution serializer
class DailyContributionSerializer(serializers.ModelSerializer):
    bank_account = BankAccountOnlySerializer(read_only=True)

    class Meta:
        model = DailyContribution
        fields = [
            "id",
            "amount",
            "bank_account",
            "balance_after_transaction",
            "TransID",
            "transaction_type",
            "created",
        ]
        read_only_field = ["created"]


# target contibution serializer
class TargetContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TargetContribution
        fields = [
            "contribution_amount",
            "contribution_type",
            "TransID",
            "created",
            "transaction_type",
        ]
        read_only_field = ["created"]


class WalletTransactionSerializer(serializers.ModelSerializer):
    account = BankAccountOnlySerializer(read_only=True)

    class Meta:
        model = WalletAccount
        fields = [
            "TransID",
            "account",
            "wallet_account",
            "amount",
            "balance_after_transaction",
            "transaction_type"
        ]
        read_only_field = ["created"]
