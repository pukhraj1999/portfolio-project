from django.db import models

# Create your models here.
class Job(models.Model):
    image=models.ImageField(upload_to='media/images/')
    summary=models.TextField()

    def __str__(self):
        return self.image