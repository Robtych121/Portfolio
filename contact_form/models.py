from django.db import models
from datetime import datetime


# Create your models here.
class ContactForm(models.Model):

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    

    name = models.CharField(max_length=254, default='')
    email = models.CharField(max_length=254, default='')
    message = models.TextField(default='')
    date = models.DateField(default=datetime.now)
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    seen = models.CharField(max_length=3, default='No',  choices=YESNOCHOICES)

    def __str__(self):
        return self.name