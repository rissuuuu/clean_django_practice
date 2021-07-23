from rest_framework.permissions import BasePermission


class AllowAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class AllowCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_customer)


class AllowDealer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_dealer)
