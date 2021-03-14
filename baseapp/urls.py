from django.urls import path
from .views import home, renewable

urlpatterns = [
    path('', home, name="home"),
    path('renewable/', renewable ,name="renewable")
]