from django.db import models
class post (models.Model):
    text = models.CharField(max_length=450)
    img = models.ImageField(upload_to= "media/",default="")
    product_name = models.CharField(max_length=50 , default="shirt")
    prize = models.IntegerField(default=499)

    def __str__(self):
        return self.product_name
class User(models.Model):
    full_name = models.CharField(max_length=70 ,default= "hritik")
    email = models.EmailField(unique=True , default="77")
    password = models.CharField(max_length=200,default="")
    cart_id = models.CharField(max_length=2000, default="")
    def __str__(self):
        return self.full_name
    
 



# Create your models here.
