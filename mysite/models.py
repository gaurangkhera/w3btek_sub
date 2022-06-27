from django.db import models
from django.contrib.auth.models import User

size=(
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
)

class Contact(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Product(models.Model):
    prod_author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    prod_name = models.CharField(max_length=50)
    prod_price = models.IntegerField(null=False, default=0)
    prod_desc = models.TextField()
    prod_date = models.DateTimeField(auto_now_add=True)
    prod_img_main = models.ImageField(upload_to='prod_img', blank=True, null=True)
    prod_img_back = models.ImageField(upload_to='prod_img', blank=True, null=True)
    prod_img_other = models.ImageField(upload_to='prod_img', blank=True, null=True)

    def __str__(self):
        return self.prod_name