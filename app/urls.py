from django.urls import path
from . import views
from .views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('balance', views.balance, name='balance'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('order', views.order, name='order'),
    path('services', views.services, name='services'),
    path('forgotPass', views.forgotPass, name='forgotPass'),
    path('news', views.news, name='news'),
    path('accounts/login', LoginView.as_view(), name="login"),
]