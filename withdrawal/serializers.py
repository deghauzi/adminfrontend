from rest_framework import serializers
from .models import WithdrawalRequest
from account.account_serializers import BankAccountOnlySerializer
from userprofile.auth_serializers import UserCreateSerializer
class WithdrawalRequestSerilizer(serializers.ModelSerializer):
    request_user = UserCreateSerializer(read_only=True)    
    request_user_account = BankAccountOnlySerializer(read_only=True)    
    class  Meta:
        model = WithdrawalRequest
        fields = "__all__"