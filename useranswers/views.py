from django.shortcuts import render
from .models import UserAnswer
from .serializers import UserAnswerSerializer
from rest_framework import viewsets


# Create your views here.
class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
