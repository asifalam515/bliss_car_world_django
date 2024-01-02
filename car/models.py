from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.
class CarModel(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    price=models.IntegerField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
   
    
    def __str__(self) -> str:
        return self.title

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)

class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"
