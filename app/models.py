from django.db import models

# Create your models here.

class Task(models.Model):
    PRIOTRY_CHOICES = [
        ('L', 'muhum'),
        ('M', 'urtacha'),
        ('H', 'shartmas'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(choices=PRIOTRY_CHOICES, default='M', max_length=1)




    def __str__(self):
        return f"Task(id={self.id}),name={self.name}"
