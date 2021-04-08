from django.db import models

# Create your models here.
class RenewableData(models.Model):
    Cityname = models.CharField(max_length=50)
    wattage = models.IntegerField()

    def __str__(self):
        return self.Cityname + str(self.wattage)

class Consumer(models.Model):
    name = models.CharField(max_length=50)
    consumer_id = models.CharField(unique=True, null=False, blank=False,max_length=50)
    sub_station = models.CharField(max_length=50)
    area_code = models.IntegerField(blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.consumer_id

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    contact_number = models.IntegerField(unique=True, null=False, blank=False)
    area_code = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

class RegisterComplaint(models.Model):
    REASON = [("Electricity Outage", "Electricity Outage"), ("Employee Complaint", "Employee Complaint"), ("Suggestions", "Suggestions")]
    consumer_id = models.CharField(unique=True, null=False, blank=False, max_length=50)
    category = models.CharField(choices=REASON, max_length=50)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[("Resolved","Resolved"),("Pending","Pending")], default="Pending")
    date = models.DateField(auto_now=True)

class Bill(models.Model):
    consumer_id = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    total_price = models.IntegerField(blank=False,null=False)
    meter_number = models.IntegerField(blank=False,null=False)