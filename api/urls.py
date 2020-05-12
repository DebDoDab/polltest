from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.views import PollViewSet
from questions.views import QuestionViewSet

router = routers.DefaultRouter()
router.register('polls', viewset=PollViewSet)
router.register('questions', viewset=QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]