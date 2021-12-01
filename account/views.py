from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.viewsets import ModelViewSet
from .account_serializers import (BankAccountSerializer,WalletAccountSerializer)
from .models import BankAccount,WalletAccount




class BankAccountAPI(ModelViewSet):
    http_method_names = ['get']
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        if self.request.user.is_staff:
            return BankAccount.objects.all()
        return self.request.user.account.all().order_by('-created')

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = BankAccount.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    
class WalletAccountAPI(ModelViewSet):
    http_method_names = ['get']
    serializer_class = WalletAccountSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return WalletAccount.objects.all()
        return self.request.user.user_bonus_acc.all().order_by('-created')

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = WalletAccount.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj


