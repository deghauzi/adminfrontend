from rest_framework import serializers
from .models import DailyContribution,TargetContribution
from account.account_serializers import BankAccountOnlySerializer



#daily contribution serializer
class DailyContributionSerializer(serializers.ModelSerializer):
    account = BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = DailyContribution
        fields = ['id','amount','account','balance_after_transaction','created_by_admin_user',
                  'transaction_type', 'created']
        read_only_field = [ 'created', 'updated']
        

#target contibution serializer
class TargetContributionSerializer(serializers.ModelSerializer):
    account= BankAccountOnlySerializer(read_only=True)
    created_by_admin_user = serializers.SlugRelatedField(read_only=True,slug_field="username")
    class Meta:
        model = TargetContribution
        fields = ['id','contribution_amount','account','contribution_type','created_by_admin_user',
                  'user', 'created','transaction_type']
        read_only_field = [ 'created', 'updated']