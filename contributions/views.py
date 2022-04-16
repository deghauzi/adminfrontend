from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import DailyContribution,TargetContribution
from .serializers import DailyContributionSerializer,TargetContributionSerializer


# Create your views here.
class DailyContributionAPI(ModelViewSet):
    http_method_names = ['get','post','patch','put']
    serializer_class = DailyContributionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return DailyContribution.objects.all()
        return self.request.user.user_account.all().order_by('created')

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = DailyContribution.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    
class TargetContributionAPI(ModelViewSet):
    http_method_names = ['get','post','put','patch']
    serializer_class = TargetContributionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return TargetContribution.objects.all()
        return self.request.user.user_contribution_acc.all().order_by('-created')

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = TargetContribution.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    