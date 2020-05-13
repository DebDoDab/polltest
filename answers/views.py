from django.shortcuts import render
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework import viewsets


# Create your views here.
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        questionId = self.request.query_params.get('question_id', None)
        if questionId is not None:
            queryset = queryset.filter(question_id=questionId)
        return queryset
