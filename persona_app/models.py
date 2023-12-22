from django.db import models


class Persona(models.Model):
    tipo_documento = models.CharField('Tipo documento', max_length=15, blank=False, null=False)
    documento = models.CharField('Documento', max_length=10, blank=False, null=False)
    nombre = models.CharField('Nombre', max_length=20, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=20, blank=False, null=False)
    hobbie = models.CharField('Hobbie', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        nombre_persona = str(self.nombre) + ' ' + str(self.apellidos)
        return nombre_persona
