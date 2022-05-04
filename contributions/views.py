from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum
import datetime
from .models import DailyContribution, TargetContribution
from .serializers import DailyContributionSerializer, TargetContributionSerializer


# Create your views here.
class UserDailyContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = DailyContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ["created"]

    def get_queryset(self):
        query = DailyContribution.objects.filter(
            approved=True, user_account=self.request.user
        )
        return query
class AllDailyContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = DailyContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ["created"]

    def get_queryset(self):
        query = DailyContribution.objects.all()
        return query


class AdminDailyContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = DailyContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ["created"]

    def list(self, request):
        query_deposite = DailyContribution.objects.filter(
            approved=True, transaction_type=1,created__gt= datetime.date.today()
        ).count()
        query_withdrawal = DailyContribution.objects.filter(
            approved=True, transaction_type=2,created__gt= datetime.date.today()
        ).count()
        total_deposit = DailyContribution.objects.filter(
            approved=True, transaction_type=1,created__gt= datetime.date.today()
        ).aggregate(Sum("amount"))
        total_withdrawal = DailyContribution.objects.filter(
            approved=True, transaction_type=2,created__gt= datetime.date.today()
        ).aggregate(Sum("amount"))
        return Response(
            {
                "deposite_count": query_deposite,
                "deposite_with": query_withdrawal,
                "query_total_depo": total_deposit,
                "total_withdrawal": total_withdrawal,
            }
        )


class TargetContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = TargetContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ["created"]

    def get_queryset(self):
        query = TargetContribution.objects.filter(
            approved=True, user_account=self.request.user
        )
        return query
class AllContributionAPI(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = TargetContributionSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ["created"]

    def get_queryset(self):
        query = TargetContribution.objects.all()
        return query
