from rest_framework.routers import DefaultRouter
from .views import (BankAccountAPI,WalletAccountAPI)

routes = DefaultRouter(trailing_slash=False)

# bank account type and wallet
routes.register('get_bank_account', BankAccountAPI, 'get-bank-account')
routes.register('get_bonus_account', WalletAccountAPI, 'get-bonus-account')


urlpatterns = [
    *routes.urls
]
