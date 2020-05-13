from django.db import models
from polls.models import Poll


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=512)
    ANSWERS_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = models.IntegerField(choices=ANSWERS_CHOICES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll')
    prevQuestion = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='prev', default=None,
                                     null=True, blank=True)
    nextQuestion = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='next', default=None,
                                     null=True, blank=True)

    def __str__(self):
        return self.text