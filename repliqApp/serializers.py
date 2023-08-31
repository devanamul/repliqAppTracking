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
    def validate(self, data):
        if self.instance and 'employee' in data:
            if self.instance.is_checked_out():
                raise serializers.ValidationError('Device is already checked out.')

        return data
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'