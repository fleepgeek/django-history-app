from django.db import models
from django.urls import reverse


class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField()
    created_on     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})

