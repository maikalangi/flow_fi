from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('exchanges/', views.ExchangeIndex.as_view(), name='exchanges_index'),
    path('exchanges/<int:pk>/', views.ExchangeDetail.as_view(), name='exchange_detail'),
    path('exchanges/create', views.ExchangeCreate.as_view(), name='exchange_create'),
    path('exchanges/<int:exchange_id>/update', views.ExchangeUpdate.as_view(), name='exchange_update'),
    path('exchanges/<int:exchange_id>/delete', views.ExchangeDelete.as_view(), name='exchange_delete'),

    path('wallets/', views.WalletIndex.as_view(), name='wallets_index'),
    path('wallets/<int:pk>/', views.WalletDetail.as_view(), name='wallet_detail'),
    path('wallets/create', views.WalletCreate.as_view(), name='wallet_create'),
    path('wallets/<int:wallet_id>/update', views.WalletUpdate.as_view(), name='wallet_update'),
    path('wallets/<int:wallet_id>/delete', views.WalletDelete.as_view(), name='wallet_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]