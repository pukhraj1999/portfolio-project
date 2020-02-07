from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='media/images/')
    description=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        # only 100 characters of description shown
        return self.description[:100]

