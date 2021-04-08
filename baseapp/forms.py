from django.forms import ModelForm
from .models import RenewableData, Consumer, Employee, RegisterComplaint

class RenewableDataForm(ModelForm):
    class Meta:
        model = RenewableData
        fields = ['Cityname', 'wattage']

class ConsumerForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['name','consumer_id','sub_station','area_code', 'email']

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','designation','contact_number','email']

class RegisterComplaintForm(ModelForm):
    class Meta:
        model = RegisterComplaint
        fields = ['consumer_id', 'category', 'description', 'address']