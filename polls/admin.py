from django.contrib import admin
from .models import Answer, Poll, Question, UserAnswer

admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(UserAnswer)
