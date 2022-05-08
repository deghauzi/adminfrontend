from rest_framework import serializers

from account.models import WalletAccount
from .models import DailyContribution, TargetContribution
from account.account_serializers import BankAccountOnlySerializer
from userprofile.auth_serializers import UserCreateSerializer

# daily contribution serializer
class DailyContributionSerializer(serializers.ModelSerializer):
    bank_account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(
        slug_field="email", read_only=True)

    class Meta:
        model = DailyContribution
        fields = [
            "amount",
            "bank_account",
            "balance_after_transaction",
            "TransID",
            "transaction_type",
            "created",
            "created_by_admin_user"
        ]
        read_only_field = ["created"]


# target contibution serializer
class TargetContributionSerializer(serializers.ModelSerializer):
    user_account = UserCreateSerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(
        slug_field="email", read_only=True)

    class Meta:
        model = TargetContribution
        fields = [
            "contribution_amount",
            "contribution_type",
            "TransID",
            "created",
            "transaction_type",
            "created_by_admin_user",
            "user_account"
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
