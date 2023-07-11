
from django.db import models
from .utils import base62_encode

# Create your models here.
class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    @staticmethod
    def generate_short_url():
        last_url = Url.objects.order_by('id').last()
        if last_url:
            last_id = last_url.id
        else:
            last_id = 1

        return base62_encode(last_id)

    def __str__(self):
        return self.long_url
