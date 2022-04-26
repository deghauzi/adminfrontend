from rest_framework.routers import DefaultRouter
from .views import (UserBankAccountAPI,UserWalletAccountAPI)

routes = DefaultRouter(trailing_slash=False)

# bank account type and wallet
routes.register('get_bank_account', UserBankAccountAPI, 'get-bank-account')
routes.register('get_bonus_account', UserWalletAccountAPI, 'get-bonus-account')


urlpatterns = [
    *routes.urls
]
