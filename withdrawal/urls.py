from django.urls import path
from .views import WithdrawalRequestAPI



urlpatterns = [
    path('withdrawal', WithdrawalRequestAPI.as_view(), name='user_account'),
]
