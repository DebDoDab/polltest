from django.db import models
from questions.models import Question
from django.contrib.auth.models import User


# Create your models here.
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.IntegerField()
    stringAns = models.CharField(max_length=256)
    # TODO Add PostgreS ArrayField arrayAns
    ANSWER_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = models.IntegerField(choices=ANSWER_CHOICES)

    def __str__(self):
        return f'Answer by {self.user} - {self.stringAns}'
