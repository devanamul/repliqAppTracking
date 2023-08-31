from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'condition', 'company', 'is_checked_out']  

    def get_is_checked_out(self, obj):
        return obj.is_checked_out()
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        # exclude = ['return_date']
        fields = '__all__'