from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login

class LoginView(View):

    template = 'login.html'

    def get(self, request, *args, **kwargs):

        return render(request, template_name=self.template)

    def post(self, request, *args, **kwargs):

        username = 'anon'

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('comment:comment')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid password')

        return render(request, template_name=self.template)