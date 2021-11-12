from rest_framework.routers import DefaultRouter
from .views import (LoginViewSet, RegistrationViewSet, RefreshViewSet,UserViewSet,
    GetBankAccountViewSet,GetTransactionViewSet,GetContributionSerializerViewSet,GetBonusAccountViewSet)


routes = DefaultRouter(trailing_slash=False)

# AUTHENTICATION
routes.register(r'login', LoginViewSet, basename='auth-login')
routes.register(r'register', RegistrationViewSet, basename='auth-register')
routes.register(r'refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'get_bank_account', GetBankAccountViewSet, basename='get-bank-account')
routes.register(r'get_bonus_account', GetBonusAccountViewSet, basename='get-bonus-account')
routes.register(r'get_trans', GetTransactionViewSet, basename='account-transaction')
routes.register(r'get_contribution', GetContributionSerializerViewSet, basename='account-contribution-transaction')
# USER
routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls
]
