from django.db import models
from django.urls import reverse
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100, null=True)
    rate = models.IntegerField(null=True)
    quantity= models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk': self.pk})