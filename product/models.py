from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):

    CONDITION_TYPE=(
        ("New", "NEW"),
        ("Used","Used")

    )
    #contain all the products information
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Category(models.Model):
    #for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.category_name