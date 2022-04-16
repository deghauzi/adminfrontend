from rest_framework import serializers

from account.models import WalletAccount
from .models import DailyContribution, TargetContribution
from account.account_serializers import BankAccountOnlySerializer


# daily contribution serializer
class DailyContributionSerializer(serializers.ModelSerializer):
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = DailyContribution
        fields = [
            "id",
            "amount",
            "account",
            "balance_after_transaction",
            "created_by_admin_user",
            "TransID",
            "transaction_type",
            "created",
        ]
        read_only_field = ["created", "updated"]


# target contibution serializer
class TargetContributionSerializer(serializers.ModelSerializer):
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = TargetContribution
        fields = [
            "id",
            "contribution_amount",
            "account",
            "contribution_type",
            "created_by_admin_user",
            "TransID",
            "created",
            "transaction_type",
        ]
        read_only_field = ["created", "updated"]


class WalletTransactionSerializer(serializers.ModelSerializer):
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = WalletAccount
        fields = [
            "id",
            "TransID",
            "account",
            "wallet_account",
            "amount",
            "balance_after_transaction",
            "transaction_type",
            "created_by_admin_user",
        ]
        read_only_field = ["created", "updated"]
