from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (UserDailyContributionAPI,TargetContributionAPI)

routes = DefaultRouter(trailing_slash=False)

# Transactions
routes.register('get_daily_trans', UserDailyContributionAPI, 'daily-account-transaction')
routes.register('get_target_trans', TargetContributionAPI, 'target-account-transaction')



urlpatterns = [
    *routes.urls
]
