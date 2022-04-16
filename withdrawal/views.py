from rest_framework import generics, permissions
from .serializers import WithdrawalRequestSerilizer
from .models import WithdrawalRequest
from account.models import BankAccount


class WithdrawalRequestAPI(generics.ListCreateAPIView):
    serializer_class = WithdrawalRequestSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        account = BankAccount.objects.get(user_profile=self.request.user)
        serializer.save(request_user=self.request.user,
                        request_user_account=account)

    def get_queryset(self):
        return self.request.user.request_withdrawal.all().prefetch_related('request_user').order_by("created")


# Create your views here.
