from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(blank=False,upload_to='images/')
    link = models.URLField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
