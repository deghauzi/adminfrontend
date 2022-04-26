from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .account_serializers import BankAccountSerializer, WalletAccountSerializer
from .models import BankAccount, WalletAccount
from rest_framework.response import Response
from rest_framework import status


class UserBankAccountAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query = self.request.user.account.prefetch_related("user_profile")
        return query

 

class UserWalletAccountAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = WalletAccountSerializer
    queryset = WalletAccount.objects.all()
    permission_classes = (IsAuthenticated,)


    def list(self, request):
        query = WalletAccount.objects.get(user=request.user)
        serializer = self.serializer_class(query)
        return Response(
            {"status": True, "data": serializer.data}, status=status.HTTP_200_OK
        )

