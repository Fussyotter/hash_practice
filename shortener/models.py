from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.