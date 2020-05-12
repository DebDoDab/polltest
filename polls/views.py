from django.shortcuts import render
from rest_framework import viewsets
from .models import Poll
from .serializers import PollSerializer


# Create your views here.
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer