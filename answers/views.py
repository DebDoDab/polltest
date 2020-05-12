from django.shortcuts import render
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework import viewsets


# Create your views here.
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
