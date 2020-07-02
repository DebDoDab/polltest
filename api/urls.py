from django.urls import path, include
from polls.views import AnswerViewSet, PollViewSet, QuestionViewSet, UserAnswerViewSet, getStats
from rest_framework import routers

router = routers.DefaultRouter()
router.register('answers', viewset=AnswerViewSet)
router.register('polls', viewset=PollViewSet)
router.register('questions', viewset=QuestionViewSet)
router.register('useranswers', viewset=UserAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('getstats', getStats),
]