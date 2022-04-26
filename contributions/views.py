from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import DailyContribution, TargetContribution
from .serializers import DailyContributionSerializer, TargetContributionSerializer


# Create your views here.
class UserDailyContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = DailyContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['created']

    def get_queryset(self):
        query = DailyContribution.objects.filter(user_account=self.request.user)
        return query


class TargetContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = TargetContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['created']

    def get_queryset(self):
        query = TargetContribution.objects.filter(user_account=self.request.user)
        return query
