from django.urls import path
from user.views import *

urlpatterns = [
    path('auth/registration', UserCreate.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('auth/user', AuthUserView.as_view()),
    path('auth/user/list', UserListView.as_view()),
]
