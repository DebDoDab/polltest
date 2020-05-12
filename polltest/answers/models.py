from django.db import models
from polltest.questions.models import Question


# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
