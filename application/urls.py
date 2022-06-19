from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from application.views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('order/create', CreateOrderView.as_view(), name='order_create')
]