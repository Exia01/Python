import random
from .methods import get_filename_ext
from django.db import models


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 8989898989898)
    print('from upload, instance:', instance)
    print('from upload, filename:',filename, '\n')
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}-{ext}'
    # file will be uploaded to MEDIA_ROOT
    return f'products/{new_filename}/{final_filename}'


class Product(models.Model):  # ProductCategory
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=25, default=0.00)
    # null is for the db, blank is for django
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):  # a method
        return self.title

# if python -V < 3.6
 ## final_filename = '{new_filename}-{ext}'.format(new_filename=new_filename, ext=ext)
 # return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)
