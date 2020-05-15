from django.db import models

# Create your models here.
class main_portfolio(models.Model):

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