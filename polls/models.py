from django.db import models


# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=256)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name
