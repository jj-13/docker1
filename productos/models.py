from django.db import models
from base.models import BaseModel


class Product(BaseModel):
    name = models.CharField('Producto', max_length=25, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion', blank=False, null=False)
    image = models.ImageField('Imagen', upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

