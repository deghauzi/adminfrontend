from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserDailyContributionAPI,
    TargetContributionAPI,
    AllDailyContributionAPI,
    AdminDailyContributionAPI,
    AllContributionAPI,
)

routes = DefaultRouter(trailing_slash=False)

# Transactions
routes.register("get_daily_trans", UserDailyContributionAPI, "daily-account-transaction")
routes.register("get_target_trans", TargetContributionAPI, "target-account-transaction")
routes.register("get_admin_count_trans", AdminDailyContributionAPI, "get_admin_count_trans")
routes.register("get_daily_all_trans", AllDailyContributionAPI, "get_daily_all_trans")
routes.register("get_target_all_trans", AllContributionAPI, "get_target_all_trans")


urlpatterns = [*routes.urls]
