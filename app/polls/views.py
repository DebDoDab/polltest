from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Answer, Poll, Question, UserAnswer
from .serializers import AnswerSerializer, PollSerializer, QuestionSerializer, UserAnswerSerializer
from .services import get_statistics


def get_stats(request):
    """Returns page with JSON statistic for a given user"""
    user_id = request.GET.get('user_id')
    if not user_id.isdecimal():
        raise Http404
    user_id = int(user_id)
    return HttpResponse(get_statistics(user_id))


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for Answer model"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        question_id = self.request.query_params.get('question_id', None)
        if question_id is not None:
            queryset = queryset.filter(question_id=question_id)
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
        first_from = self.request.query_params.get('first_from', None)
        poll_id = self.request.query_params.get('poll_id', None)
        if first_from is not None:
            queryset = queryset.filter(poll_id=first_from, prev=None)
        elif poll_id is not None:
            queryset = queryset.filter(poll_id=poll_id)

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
