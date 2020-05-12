from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.views import PollViewSet
from questions.views import QuestionViewSet
from answers.views import AnswerViewSet
from useranswers.views import UserAnswerViewSet

router = routers.DefaultRouter()
router.register('polls', viewset=PollViewSet)
router.register('questions', viewset=QuestionViewSet)
router.register('answers', viewset=AnswerViewSet)
router.register('useranswers', viewset=UserAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]