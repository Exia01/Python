import random
from .methods import get_filename_ext
from django.db import models
from .customQueries import ProductQuerySet

from django.db.models.signals import pre_save, post_save
from .signals import product_pre_save_receiver


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 8989898989898)
    # print('from upload, instance:', instance)
    # print('from upload, filename:', filename, '\n')
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}-{ext}'
    # file will be uploaded to media_root/products/name
    return f'products/{new_filename}/{final_filename}'


# performs custom query methods 
class ProductManager(models.Manager):
    def get_queryset(self): #overwritting the reg get query method 
        return ProductQuerySet(self.model, using=self._db)

    # named specific queries or model manager queries
    # def features(self): ### Product.objects.featured()
    #     return self.get_queryset().featured()

    # def all(self): ### Product.objects.all()
    #     return self.get_queryset().active()

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id)
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None




class Product(models.Model):  
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=25, default=0.00)
    # null is for the db, blank is for django
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=False)
    
    objects = ProductManager()  # wrapping it or "extending it"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.slug)])

    def __str__(self):  # a method
        return self.title


pre_save.connect(product_pre_save_receiver, sender=Product) 


# if python -V < 3.6
 ## final_filename = '{new_filename}-{ext}'.format(new_filename=new_filename, ext=ext)
 # return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)
