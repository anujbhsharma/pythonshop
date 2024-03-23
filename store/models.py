from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=230, db_index=True)
    slug = models.SlugField(max_length=230, unique=True)
    
    class Meta:
        
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list_category', args=[self.slug])
    
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=230)
    brand = models.CharField(max_length=230,default='N/A')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=230)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='images/', blank=True)    

    class Meta:
        verbose_name_plural = 'products'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_info', args=[self.slug])
    
    
    
    
    