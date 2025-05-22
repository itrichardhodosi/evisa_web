from django.db import models
from django.urls import reverse

class Category(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug   = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo         = models.CharField(max_length=200)
    slug           = models.SlugField(max_length=200, unique=True)
    categoria      = models.ForeignKey(Category, on_delete=models.PROTECT)
    extracto       = models.CharField(max_length=300)
    contenido      = models.TextField()
    imagen         = models.ImageField(upload_to='posts/', null=True, blank=True)
    publicado      = models.DateTimeField(auto_now_add=True)
    actualizado    = models.DateTimeField(auto_now=True)
    publicado_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.titulo
