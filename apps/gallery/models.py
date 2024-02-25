from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

class Photography(models.Model):

    CATEGORY_OPTIONS = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    name = models.CharField(max_length=50, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=15, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    address = models.ImageField(upload_to="photographs/%Y/%m", blank=True)
    published = models.BooleanField(default=True)
    release_date = models.DateField(default=datetime.now, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')
    

    def __str__(self):
        return self.name