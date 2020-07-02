from django.db import models


class Poll(models.Model):
    """Model for polls"""
    name = models.CharField(max_length=256, verbose_name="Poll name")
    start_date = models.DateTimeField(verbose_name="Date and time of opening the poll")
    end_date = models.DateTimeField(verbose_name="Date and time of closing the poll")
    description = models.CharField(max_length=512, verbose_name="Poll description")

    def __str__(self):
        return self.name


class Question(models.Model):
    """Model for questions with answers and some adjacent info"""
    text = models.CharField(max_length=512, verbose_name="Question text")
    ANSWERS_TYPE_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = models.IntegerField(choices=ANSWERS_TYPE_CHOICES, verbose_name="Type of answering the question")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll',
                             verbose_name="Link to the adjacent poll")
    prev_question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='prev', default=None,
                                      null=True, blank=True, verbose_name="Link to the previous question")
    next_question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='next', default=None,
                                      null=True, blank=True, verbose_name="Link to the next question")

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Model for answers"""
    text = models.CharField(max_length=256, verbose_name="Text of an answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Link to the adjacent question")

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    """Model for storage users' answers"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Link to the adjacent question")
    user = models.IntegerField(verbose_name="Id of adjacent user")
    string_ans = models.CharField(max_length=256, verbose_name="User's answer")
    # TODO Add PostgreS ArrayField arrayAns
    # Maybe it's better to take type from adjacent question?
    type = models.IntegerField(choices=Question.ANSWERS_TYPE_CHOICES, verbose_name="Type of answering the question")

    def __str__(self):
        return f'Answer by {self.user} - {self.string_ans}'
