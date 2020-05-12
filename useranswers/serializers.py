from rest_framework import serializers
from .models import UserAnswer


class UserAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    stringAns = serializers.CharField(max_length=256)
    ANSWER_CHOICES = [
        (0, 'Enter your string'),
        (1, 'Choose one answer'),
        (2, 'Choose several answers'),
    ]
    type = serializers.ChoiceField(choices=ANSWER_CHOICES)

    class Meta:
        model = UserAnswer
        fields = ['id', 'question', 'user', 'stringAns', 'type']
