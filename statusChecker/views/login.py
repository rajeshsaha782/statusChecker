from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class LoginView(LoginView):
    def get(self, request, **kwargs):
        return render(request, 'login.html')

    def post(self, request, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # request.session['user'] = user.id
            # print(request.session['user'])
            return redirect('/')
        return render(request, 'login.html', {'message': 'Wrong Username or Password. Try Again'})
