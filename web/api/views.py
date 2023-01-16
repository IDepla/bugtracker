from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from web.models import User, Bug
from .serializers import UserSerializer, BugSerializer


class UserViewSet(ReadOnlyModelViewSet):
    """Interface the users"""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class BugViewSet(ModelViewSet):
    """Bug interface"""

    queryset = Bug.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BugSerializer
