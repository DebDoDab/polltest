from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=256)
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question']
