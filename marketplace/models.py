from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=False,default=0)
    description = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='marketplace',null=False)
    
    def __str__(self):
        return self.title