from rest_framework import viewsets

from statusChecker.models import Url
from statusChecker.serializers import UrlSerializer


class UserUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)
