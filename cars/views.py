from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CommentForm, ProfileForm
from django.contrib import messages

from .models import Car, Brand, Order, Comment

# Create your views here.
class HomeView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.GET.get('brand')
        if brand:
            queryset = queryset.filter(brand__id=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
    

class CarDetailView(View):
    def get(self, request, pk):
        car = Car.objects.get(pk=pk)
        comments = Comment.objects.filter(car=car)
        form = CommentForm()
        return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})

    def post(self, request, pk):
        car = Car.objects.get(pk=pk)
        comments = Comment.objects.filter(car=car)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            messages.success(request, "Comment added successfully")
            return redirect('car_detail', pk=car.pk)
        return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})

class BuyCarView(View):
    @method_decorator(login_required)
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car.quantity > 0:
            Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
        return redirect('profile_page')


class OrderHistoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        user_form = ProfileForm(instance=request.user)
        return render(request, 'profile.html', {'orders': orders, 'user_form': user_form})

    def post(self, request):
        orders = Order.objects.filter(user=request.user)
        user_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_page')
        return render(request, 'profile.html', {'orders': orders, 'user_form': user_form})

