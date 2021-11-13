from rest_framework.routers import DefaultRouter
from .views import (LoginViewSet, RegistrationViewSet, RefreshViewSet,UserViewSet,
    GetBankAccountViewSet,GetTransactionViewSet,GetContributionSerializerViewSet,GetBonusAccountViewSet)


routes = DefaultRouter(trailing_slash=False)

# AUTHENTICATION
routes.register('login', LoginViewSet, 'auth-login')
routes.register('register', RegistrationViewSet, 'auth-register')
routes.register('refresh', RefreshViewSet, 'auth-refresh')
routes.register('get_bank_account', GetBankAccountViewSet, 'get-bank-account')
routes.register('get_bonus_account', GetBonusAccountViewSet, 'get-bonus-account')
routes.register('get_trans', GetTransactionViewSet, 'account-transaction')
routes.register('get_contribution', GetContributionSerializerViewSet, 'account-contribution-transaction')
# USER
routes.register('user', UserViewSet, 'user')


urlpatterns = [
    *routes.urls
]
