from django.http import Http404
from rest_framework import serializers
from django.utils import timezone
from polls.models import Poll
from questions.models import Question
from .models import UserAnswer


class UserAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    questionId = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField()
    stringAns = serializers.CharField(max_length=256)
    ANSWER_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = serializers.ChoiceField(choices=ANSWER_CHOICES)

    def create(self, validated_data):
        question = Question.objects.get(id=validated_data['questionId'])
        poll = Poll.objects.get(id=question.poll_id)
        if poll.endDate < timezone.now():
            raise Http404  # TODO error Poll is over
        validated_data['question'] = validated_data['questionId']
        validated_data.pop('questionId')
        return UserAnswer.objects.create(**validated_data)

    class Meta:
        model = UserAnswer
        fields = ['id', 'question', 'user', 'stringAns', 'type', 'questionId']
