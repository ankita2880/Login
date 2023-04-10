from django.urls import path
from .views import Record, Login, Logout



urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
]