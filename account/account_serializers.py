from rest_framework import serializers
from .models import (UserAddress,UserBankAccount,BankAccountType,Transaction,Contribution,BonusAccount)
from .auth_serializers import UserSerializer


class BankAcoountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = ['id','maximum_withdrawal_amount', 'name','annual_interest_rate',
                  'interest_calculation_per_year', 'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = UserAddress
        fields = ['id','user', 'street_address','city','postal_code','country', 'created', 'updated','created_by_admin_user',]
        read_only_field = [ 'created', 'updated']
        
        
        
class BankAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    account_type = BankAcoountTypeSerializer(read_only=True)
    class Meta:
        model = UserBankAccount
        fields = ['id','user', 'account_type','account_no','account_balance','created_by_admin_user',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class TransactionSerializer(serializers.ModelSerializer):
    account = BankAccountSerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = Transaction
        fields = ['id','amount','account','balance_after_transaction','created_by_admin_user',
                  'transaction_type', 'timestamp']
        read_only_field = [ 'timestamp']
        
class BankAccountOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = ['id','user','account_balance', 'account_no','account_type','created_by_admin_user',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class BonusAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = BonusAccount
        fields = ['id','user', 'account','bonus_amount_withdrawal','total_amount','created_by_admin_user',
                  'bonus_amount_add','bonus_paid_out',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class ContributionSerializer(serializers.ModelSerializer):
    account= BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = Contribution
        fields = ['id','contribution_amount','account','contribution_type','created_by_admin_user',
                  'user', 'created', 'updated']
        read_only_field = [ 'created', 'updated']