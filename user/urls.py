from django.urls import path
from .views import SignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]