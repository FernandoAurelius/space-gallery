from django.db import models

class Photography(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Photography: name = {self.name}'