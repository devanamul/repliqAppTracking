from rest_framework import viewsets, permissions, serializers
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .permisions import IsCompanyEmployee
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsCompanyEmployee]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsCompanyEmployee]

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsCompanyEmployee]

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated, IsCompanyEmployee]

    def get_is_checked_out(self, obj):
        return obj.is_checked_out()

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        device = self.get_object()
        employee_id = request.data.get('employee_id')
        condition = request.data.get('condition')
        due_date = request.data.get('due_date')
        employee = Employee.objects.get(id=employee_id)

        DeviceLog.objects.create(
            device=device,
            employee=employee,
            condition_at_checkout=condition,
            due_date=due_date
        )
        return Response({'status': 'Device checked out'})

    @action(detail=False, methods=['get'])
    def available(self, request):
        checked_out_device_ids = DeviceLog.objects.filter(return_date__isnull=True).values_list('device_id', flat=True)
        available_devices = Device.objects.exclude(id__in=checked_out_device_ids)
        serializer = DeviceSerializer(available_devices, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        overdue_logs = DeviceLog.objects.filter(return_date__isnull=True, due_date__lt=today)
        overdue_devices = [log.device for log in overdue_logs]
        serializer = DeviceSerializer(overdue_devices, many=True)
        return Response(serializer.data)

