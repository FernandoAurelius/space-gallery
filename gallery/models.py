from django.db import models

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
    published = models.BooleanField(default=False)
    release_date = models.DateField(default=datetime.now, blank=False)
    

    def __str__(self):
        return self.name