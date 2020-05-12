from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.views import PollViewSet

router = routers.DefaultRouter()
router.register('poll', viewset=PollViewSet)

urlpatterns = [
    path('', include(router.urls)),
]