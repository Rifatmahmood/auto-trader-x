
from django.urls import path
from .views import HomeView, CarDetailView, BuyCarView, OrderHistoryView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name="home_page" ), 
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('buy/<int:pk>/', BuyCarView.as_view(), name='buy_car'),
    path('profile/', OrderHistoryView.as_view(), name='profile_page'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)