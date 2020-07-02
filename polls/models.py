from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


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


class Answer(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


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