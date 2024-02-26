from django.db import models

# Create your models here.

class Users(models.Model):
  fullname = models.CharField(max_length=200)
  username = models.CharField(max_length=50)
  email = models.EmailField()
  age = models.IntegerField(null=True)
  password = models.CharField(max_length=120)
  date = models.DateField(null=True)

  def __str__(self):
    return self.fullname


class Products(models.Model):
  product_name = models.CharField(max_length=70)
  product_price = models.CharField(max_length=100)
  product_quantity = models.IntegerField(null=True)

  def __str__(self):
    return self.product_name
