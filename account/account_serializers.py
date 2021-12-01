from rest_framework import serializers
from .models import (BankAccount,BankAccountType,WalletAccount)
from userprofile.auth_serializers import UserCreateSerializer

#account type serializer
class AcoountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = ['id', 'name','account_type_image', 'created', 'updated']
        read_only_field = [ 'created', 'updated']
        

#bank account serializer with attached users   
class BankAccountSerializer(serializers.ModelSerializer):
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    bank_account_type = AcoountTypeSerializer(read_only=True)
    user_profile = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = BankAccount
        fields = ['id', 'user_profile','bank_account_type','bank_account_no','bank_account_balance','created_by_admin_user',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']

#bank account serializers only
class BankAccountOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'bank_account_type','bank_account_no','bank_account_balance','created_by_admin_user',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
#bonus wallet account
class WalletAccountSerializer(serializers.ModelSerializer):
    # user_profile = UserCreateSerializer(read_only=True)
    user_profile = serializers.SlugRelatedField(read_only=True,slug_field="username")
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = WalletAccount
        fields = ['id','user_profile', 'account','bonus_amount_withdrawal','total_amount','created_by_admin_user',
                  'bonus_amount_add','bonus_paid_out',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']