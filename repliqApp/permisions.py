from rest_framework import permissions

class IsCompanyEmployee(permissions.BasePermission):
    """
    Custom permission to only allow employees of a company to view their own data.
    """

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'employee') and hasattr(obj, 'employees'):
            return request.user.employee.company == obj
        return False
