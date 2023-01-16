from rest_framework import serializers

from web.models import Bug, User


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class BugSerializer(serializers.HyperlinkedModelSerializer):
    """Bugs serializer"""

    class Meta:
        model = Bug
        fields = "__all__"
