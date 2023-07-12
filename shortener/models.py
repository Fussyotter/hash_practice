
from django.db import models
from .utils import base62_encode

class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    @staticmethod
    def generate_short_url():
        last_url = Url.objects.order_by('-id').first()
        if last_url:
            last_id = str(last_url.id)
        else:
            last_id = '1'

        while True:
            short_url = base62_encode(last_id)
            if not Url.objects.filter(short_url=short_url).exists():
                break
            last_id += '1'

        return short_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.long_url