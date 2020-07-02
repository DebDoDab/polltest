import useranswers
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.views import AnswerViewSet, PollViewSet, QuestionViewSet, UserAnswerViewSet

router = routers.DefaultRouter()
router.register('polls', viewset=PollViewSet)
router.register('questions', viewset=QuestionViewSet)
router.register('answers', viewset=AnswerViewSet)
router.register('useranswers', viewset=UserAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getstats', useranswers.views.getStats),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
]