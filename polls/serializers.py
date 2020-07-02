from django.http import Http404
from django.utils import timezone
from rest_framework import serializers
from .models import Answer, Poll, Question, UserAnswer


class PollSerializer(serializers.ModelSerializer):
    """Serializer for Poll model"""
    name = serializers.CharField(max_length=256)
    startDate = serializers.DateTimeField(read_only=True)
    endDate = serializers.DateTimeField()
    description = serializers.CharField(max_length=512)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'startDate', 'endDate', 'description']


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for Answer model"""
    text = serializers.CharField(max_length=256)
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    questionId = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data['question'] = validated_data['questionId']
        validated_data.pop('questionId')
        return Answer.objects.create(**validated_data)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question', 'questionId']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for Question model"""
    text = serializers.CharField(max_length=512)
    type = serializers.ChoiceField(choices=Question.ANSWERS_TYPE_CHOICES)
    poll = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    pollId = serializers.IntegerField(write_only=True)
    prev = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)
    prevId = serializers.IntegerField(write_only=True)
    next = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)
    nextId = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data['poll'] = validated_data['pollId']
        validated_data['next'] = validated_data['nextId']
        validated_data['prev'] = validated_data['prevId']
        validated_data.pop('pollId')
        validated_data.pop('prevId')
        validated_data.pop('nextId')
        return Question.objects.create(**validated_data)

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'poll', 'next', 'prev', 'pollId', 'nextId', 'prevId']


class UserAnswerSerializer(serializers.ModelSerializer):
    """Serializer for UserAnswer model"""
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    questionId = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField()
    stringAns = serializers.CharField(max_length=256)
    type = serializers.ChoiceField(choices=Question.ANSWERS_TYPE_CHOICES)

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