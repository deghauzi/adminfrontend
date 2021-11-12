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
    class Meta:
        model = UserAddress
        fields = ['id','user', 'street_address','city','postal_code','country', 'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
        

        
class TransactionSerializer(serializers.ModelSerializer):
    # account = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Transaction
        fields = ['id','amount','account','balance_after_transaction',
                  'transaction_type', 'timestamp']
        read_only_field = [ 'timestamp']
        
        
class BankAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    account_type = BankAcoountTypeSerializer(read_only=True)
    account = TransactionSerializer(read_only=True)
    class Meta:
        model = UserBankAccount
        fields = ['id','user', 'account_type','account','gender','birth_date','account_no','interest_start_date',
                  'initial_deposit_date','created', 'updated']
        read_only_field = [ 'created', 'updated']
        
        
class BankAccountOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = ['id','gender','birth_date','interest_start_date', 'account_no',
                  'initial_deposit_date','created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class BonusAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    account = BankAccountOnlySerializer(read_only=True)
    class Meta:
        model = BonusAccount
        fields = ['id','user', 'account','bonus_amount_withdrawal','total_amount',
                  'bonus_amount_add','bonus_paid_out',
                  'created', 'updated']
        read_only_field = [ 'created', 'updated']
        
class ContributionSerializer(serializers.ModelSerializer):
    account= BankAccountOnlySerializer(read_only=True)
    class Meta:
        model = Contribution
        fields = ['id','contribution_amount','account','contribution_type',
                  'user', 'created', 'updated']
        read_only_field = [ 'created', 'updated']