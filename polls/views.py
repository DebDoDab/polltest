from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Answer, Poll, Question, UserAnswer
from .serializers import AnswerSerializer, PollSerializer, QuestionSerializer, UserAnswerSerializer
from .services import getStatistics


def getStats(request):
    """Returns page with JSON statistic for a given user"""
    userId = request.GET.get('user_id')
    if not userId.isdecimal():
        raise Http404
    userId = int(userId)
    return HttpResponse(getStatistics(userId))


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for Answer model"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        questionId = self.request.query_params.get('question_id', None)
        if questionId is not None:
            queryset = queryset.filter(question_id=questionId)
        return queryset


class PollViewSet(viewsets.ModelViewSet):
    """ViewSet for Poll model"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        queryset = Poll.objects.all()
        active = self.request.query_params.get('active', None)
        if active is not None:
            queryset = queryset.filter(endDate__gt=timezone.now())
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for Question model"""
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
    """ViewSet for UserAnswer model"""
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    # Allows creating UserAnswer instance everybody, keeping information viewable only to admins
    permission_classes_by_action = {'create': [AllowAny]}

    def get_permissions(self):
        """Custom permission"""
        try:
            # Allows creating anybody
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # otherwise (if it's not creating) return default permissions
            return [permission() for permission in self.permission_classes]
