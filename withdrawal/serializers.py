from rest_framework import serializers
from .models import WithdrawalRequest

class WithdrawalRequestSerilizer(serializers.ModelSerializer):
    class  Meta:
        model = WithdrawalRequest
        fields = "__all__"