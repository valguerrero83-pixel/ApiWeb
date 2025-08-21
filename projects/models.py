from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200) # Caraccteres maximo 200
    contenido = models.TextField() # Textos largos sin limites
    f_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)

