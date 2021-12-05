from rest_framework import serializers
from .models import WithdrawalRequest
from account.account_serializers import BankAccountOnlySerializer
class WithdrawalRequestSerilizer(serializers.ModelSerializer):
    class  Meta:
        model = WithdrawalRequest
        fields = "__all__"