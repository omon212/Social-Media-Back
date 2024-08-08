from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    # path('logout/', UserLogoutView.as_view())
]
