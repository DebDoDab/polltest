from rest_framework import serializers
from .models import Question
from polls.models import Poll


class QuestionSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=512)
    ANSWERS_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = serializers.ChoiceField(choices=ANSWERS_CHOICES)
    poll = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'poll']
