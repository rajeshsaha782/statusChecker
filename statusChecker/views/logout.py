from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import generic


class LogoutView(generic.DetailView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect('/login/')