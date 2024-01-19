from django.db import models

class Task(models.Model):
    DAILY = 'Dnevni'
    WEEKLY = 'Tjedni'
    MONTHLY = 'Mjesečni'
    YEARLY='Godišnji'

    CATEGORY_CHOICES = [
        (DAILY, 'Dnevni'),
        (WEEKLY, 'Tjedni'),
        (MONTHLY, 'Mjesecni'),
        (YEARLY, 'Godišnji')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
