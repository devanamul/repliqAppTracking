from django.urls import path, include
from rest_framework.routers import DefaultRouter
from repliqApp.views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'device-logs', DeviceLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # ... your other url patterns
]