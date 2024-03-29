from django.db import models

# Create your models here.

class Task(models.Model):
    texte = models.CharField(max_length=200, )
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modificated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.texte

