from rest_framework import generics,permissions
from .serializers import WithdrawalRequestSerilizer
from .models import WithdrawalRequest

class WithdrawalRequestAPI(generics.ListCreateAPIView):
    serializer_class = WithdrawalRequestSerilizer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WithdrawalRequest.objects.all().order_by('created')
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(request_user=self.request.user)

    
    def get_queryset(self):
        return self.request.user.request_withdrawal.all()

# Create your views here.
