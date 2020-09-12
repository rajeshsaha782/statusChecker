from django.contrib.auth import get_user_model
from rest_framework import serializers

from statusChecker.models import Url


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UrlSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        _mutable = data._mutable
        data._mutable = True
        data['user'] = self.context['request'].user.id
        data._mutable = _mutable
        return super().to_internal_value(data)

    class Meta:
        model = Url
        fields = '__all__'
