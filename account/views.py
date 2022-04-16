from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.viewsets import ModelViewSet
from .account_serializers import (BankAccountSerializer,WalletAccountSerializer)
from .models import BankAccount,WalletAccount
from rest_framework.response import Response
from rest_framework import status



class BankAccountAPI(ModelViewSet):
    http_method_names = ['get']
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return self.request.user.account.all().order_by('-created')

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = BankAccount.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    
class WalletAccountAPI(ModelViewSet):
    http_method_names = ['get']
    serializer_class = WalletAccountSerializer
    queryset = WalletAccount.objects.all().prefetch_related('user')
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        if request.user.is_staff:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            query = WalletAccount.objects.get(user=request.user).prefetch_related('user')
            serializer = self.serializer_class(query)
            return Response({"status": True,"data": serializer.data}, status=status.HTTP_200_OK)

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = WalletAccount.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj


