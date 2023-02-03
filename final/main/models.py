from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ManyToManyField('OrderUser', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class OrderUser(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
