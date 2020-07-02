from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Answer, Poll, Question, UserAnswer
from .serializers import AnswerSerializer, PollSerializer, QuestionSerializer, UserAnswerSerializer
from .services import getStatistics


def getStats(request):
    userId = request.GET.get('user_id')
    if not userId.isdecimal():
        raise Http404
    userId = int(userId)
    return HttpResponse(getStatistics(userId))


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        questionId = self.request.query_params.get('question_id', None)
        if questionId is not None:
            queryset = queryset.filter(question_id=questionId)
        return queryset


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        queryset = Poll.objects.all()
        active = self.request.query_params.get('active', None)
        if active is not None:
            queryset = queryset.filter(endDate__gt=timezone.now())
        return queryset


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


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes_by_action = {'create': [AllowAny]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
