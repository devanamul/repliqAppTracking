from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CONDITION_CHOICES = (
    ('New', 'New'),
    ('Used', 'Used'),
    ('Damaged', 'Damaged'),
    )

class Company(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='companies')
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
    
class Device(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')
    def is_checked_out(self):
        return DeviceLog.objects.filter(device=self, return_date__isnull=True).exists()

    def __str__(self):
        return self.name
    
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_at_checkout = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    return_condition = models.CharField(max_length=255, null=True, blank=True, choices=CONDITION_CHOICES)
    due_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.device.name} - {self.employee.name}"
    def is_overdue(self):
        return not self.is_returned and self.due_date < timezone.now().date()
    
