from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserDailyContributionAPI,
    TargetContributionAPI,
    AllDailyContributionAPI,
    AdminDailyContributionAPI,
    AllContributionAPI,
    AdminTargetContributionAPI
)

routes = DefaultRouter(trailing_slash=False)

# Transactions
routes.register("get_daily_trans", UserDailyContributionAPI, "daily-account-transaction")
routes.register("get_target_trans", TargetContributionAPI, "target-account-transaction")
routes.register("get_daily_today_data",
                AdminDailyContributionAPI, "get_daily_today_data")
routes.register("get_daily_all_trans", AllDailyContributionAPI, "get_daily_all_trans")
routes.register("get_target_all_trans", AllContributionAPI, "get_target_all_trans")
routes.register("get_target_today_data",
                AdminTargetContributionAPI, "get_target_today_data")


urlpatterns = [*routes.urls]
