from django.db import models
from polltest.polls.models import Poll


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=512)
    ANSWERS_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = models.IntegerField(choises=ANSWERS_CHOICES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
