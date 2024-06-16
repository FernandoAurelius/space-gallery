from django.urls import path
from apps.users.views import login, logout, registration

urlpatterns = [
    path("login", login, name="login"),
    path("registration", registration, name="registration"),
    path("logout", logout, name="logout"),
]
