from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm

class SignupView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signed Up Successfully")
            return redirect('login')
        return render(request, 'auth/signup.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, 'auth/login.html', {'form': form})
        else:
            return redirect('home_page')

    def post(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                raw_password = form.cleaned_data['password']
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect('musician_list')
            return render(request, 'auth/login.html', {'form': form})
        else:
            return redirect('home_page')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.warning(request, "Logged Out Successfully")
        return redirect('login_page')
