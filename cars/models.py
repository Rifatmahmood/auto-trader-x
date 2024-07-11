from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField(default=2000)  # Add the model_year field
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f'Comment by {self.name} on {self.car.title}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user.username} for {self.car.title}'
