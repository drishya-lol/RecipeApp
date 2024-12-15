from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=300)
    ingredients = models.TextField()
    process = models.TextField()
    image = models.FileField(upload_to='recipes/' ,null=True, blank=True, default='default.jpg')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name    
