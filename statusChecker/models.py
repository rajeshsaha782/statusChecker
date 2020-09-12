from django.contrib.auth import get_user_model
from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=255)
    status = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'urls'
