from django.urls import path

from apps.user import views
from apps.user.views import Login, logout_view, HomeView, Sign

urlpatterns = [
    path('', Login.as_view(),name='login_view'),
    path('hello',views.home),
    path('login_view/', Login.as_view(),name='login_view'),
    path('sign/', Sign.as_view(), name='signup'),
    path('logout/user/', logout_view, name='logout_user'),
    path('dashboard/', HomeView.as_view(), name='home'),
]