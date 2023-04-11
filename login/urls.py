from django.urls import path
# from .views import Record, Login, Logout
from . import views




urlpatterns = [
    path('api/login/', views.UserLogin.as_view(), name="login"),

]