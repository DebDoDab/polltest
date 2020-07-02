from django.http import Http404
from django.utils import timezone
from rest_framework import serializers
from .models import Answer, Poll, Question, UserAnswer


class PollSerializer(serializers.ModelSerializer):
    """Serializer for Poll model"""
    name = serializers.CharField(max_length=256)
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=512)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'start_date', 'end_date', 'description']


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for Answer model"""
    text = serializers.CharField(max_length=256)
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    question_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data['question'] = validated_data['question_id']
        validated_data.pop('question_id')
        return Answer.objects.create(**validated_data)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question', 'question_id']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for Question model"""
    text = serializers.CharField(max_length=512)
    type = serializers.ChoiceField(choices=Question.ANSWERS_TYPE_CHOICES)
    poll = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    poll_id = serializers.IntegerField(write_only=True)
    prev = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)
    prev_id = serializers.IntegerField(write_only=True)
    next = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)
    next_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data['poll'] = validated_data['poll_id']
        validated_data['next'] = validated_data['next_id']
        validated_data['prev'] = validated_data['prev_id']
        validated_data.pop('poll_id')
        validated_data.pop('prev_id')
        validated_data.pop('next_id')
        return Question.objects.create(**validated_data)

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'poll', 'next', 'prev', 'poll_id', 'next_id', 'prev_id']


class UserAnswerSerializer(serializers.ModelSerializer):
    """Serializer for UserAnswer model"""
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    question_id = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField()
    string_ans = serializers.CharField(max_length=256)
    type = serializers.ChoiceField(choices=Question.ANSWERS_TYPE_CHOICES)

    def create(self, validated_data):
        question = Question.objects.get(id=validated_data['question_id'])
        poll = Poll.objects.get(id=question.poll_id)
        if poll.end_date < timezone.now():
            raise Http404  # TODO error Poll is over
        validated_data['question'] = validated_data['question_id']
        validated_data.pop('question_id')
        return UserAnswer.objects.create(**validated_data)

    class Meta:
        model = UserAnswer
        fields = ['id', 'question', 'user', 'string_ans', 'type', 'question_id']
