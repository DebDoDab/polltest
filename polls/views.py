from django.shortcuts import render
from rest_framework import viewsets
from .models import Poll
from .serializers import PollSerializer
from django.utils import timezone


# Create your views here.
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        queryset = Poll.objects.all()
        active = self.request.query_params.get('active', None)
        if active is not None:
            queryset = queryset.filter(endDate__gt=timezone.now())
        return queryset
