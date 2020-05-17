from django.db import models
from datetime import datetime

# Create your models here.
class Portfolios(models.Model):

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=254, default='')
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    published = models.CharField(max_length=3, default='No', choices=YESNOCHOICES)
    order = models.IntegerField(default=0)
    created_date = models.DateField(default=datetime.now)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='projects/', default='')
    features = models.TextField(default='')
    demolink = models.CharField(max_length=254, default='')


    def __str__(self):
        return self.name
