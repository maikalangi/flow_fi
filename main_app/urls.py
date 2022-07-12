from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('exchanges/', views.ExchangeIndex.as_view(), name='exchanges_index'),
    path('exchanges/<int:exchange_id>/', views.ExchangeDetail.as_view(), name='exchange_detail'),
    path('wallets/', views.WalletIndex.as_view(), name='wallets_index'),
    path('exchanges/<int:wallet_id>/', views.WalletDetail.as_view(), name='wallet_detail'),
]