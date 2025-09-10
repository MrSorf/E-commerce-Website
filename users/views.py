from rest_framework import viewsets, permissions
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can CRUD users