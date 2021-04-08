from django.urls import path
from .views import home, renewable, complaint, bill, power_factor, register, employee_filter, current_load

urlpatterns = [
    path('', home, name="home"),
    path('renewable/', renewable ,name="renewable"),
    path('complaint/', complaint, name="complaint"),
    path('bill/', bill, name="bill"),
    path('power_factor/', power_factor, name="power_factor"),
    path('current_load/', current_load, name="current_load"),
    path('register/', register, name='register'),
    path('employeefilter', employee_filter, name="employee_filter"),
    # path('things_speak/', things_speak, name="things_speak")
]