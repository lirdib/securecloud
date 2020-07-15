from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE,     related_name="datei", null=True)
  file = models.FileField(upload_to="data/files/", null=True, blank =True)
  name = models.CharField(max_length=200)
  uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Files'
