import threading

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from statusChecker.models import Url


def check_url_status(instance: Url):
    res = requests.get(instance.url)
    instance.status = res.status_code
    instance.save()


@receiver(post_save, sender=Url, dispatch_uid='on_url_add')
def on_url_add(sender, **kwargs):
    if kwargs['created']:
        instance: Url = kwargs['instance']
        x = threading.Thread(target=check_url_status, args=(instance,))
        x.start()
