from django.shortcuts import render

from statusChecker.models import Url


def index(request):
    urls = Url.objects.filter(user=request.user).order_by('-id')
    return render(request, 'index.html', {'name': request.user.username, 'url_list': urls})
