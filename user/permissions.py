from rest_framework.permissions import BasePermission
from constants import ADMIN_ROLE, APPLICANT_ROLE

class IsAdminGroup(BasePermission):
    """
    Custom permission to grant access only to users in the 'admin' group.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and belongs to the 'admin' group
        return request.user and request.user.is_authenticated and request.user.groups.filter(name=ADMIN_ROLE).exists()


class IsApplicantGroup(BasePermission):
    """
    Custom permission to grant access only to users in the 'applicant' group.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and belongs to the 'applicant' group
        return request.user and request.user.is_authenticated and request.user.groups.filter(name=APPLICANT_ROLE).exists()