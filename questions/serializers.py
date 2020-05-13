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
