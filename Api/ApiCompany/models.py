from django.db import models

# Create your models here.
class Catalogo(models.Model):
  tipo= models.CharField(max_length=50)
  tallas=models.CharField(max_length=10)
  color=models.CharField(max_length=20)
  stock=models.IntegerField(blank=False, null=False)


