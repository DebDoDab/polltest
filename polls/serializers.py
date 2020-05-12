from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=256)
    startDate = serializers.DateTimeField()
    endDate = serializers.DateTimeField()
    description = serializers.CharField(max_length=512)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'startDate', 'endDate', 'description']