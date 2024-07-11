from django.contrib import admin

# Register your models here.
from .models import Brand, Car, Comment, Order

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Order)