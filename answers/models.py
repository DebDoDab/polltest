from django.db import models
from questions.models import Question


# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
