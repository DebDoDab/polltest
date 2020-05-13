from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.shortcuts import render
from .serializers import QuestionSerializer
from .models import Question
from rest_framework import viewsets


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        user = self.request.user
        firstFrom = self.request.query_params.get('first_from', None)
        pollId = self.request.query_params.get('poll_id', None)
        if firstFrom is not None:
            queryset = queryset.filter(poll_id=firstFrom, prev=None)
        elif pollId is not None:
            queryset = queryset.filter(poll_id=pollId)

        return queryset
# TODO add isadminoranonreadonly
