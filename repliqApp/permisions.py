from rest_framework import permissions

class IsCompanyEmployee(permissions.BasePermission):
    """
    Custom permission to only allow companies to view their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the logged in user's company matches the object's company
        return obj.company == request.user.company.employee
    