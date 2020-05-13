from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
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
