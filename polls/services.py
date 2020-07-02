from django.http import Http404, HttpResponse
from polls.models import Answer, Poll, Question, UserAnswer
import json


def getStatistics(userId):
    """Get all answered questions for given user"""
    class AnswerTemp:
        def __init__(self, text, answerId=None):
            self.id = answerId
            self.text = text

    class QuestionTemp:
        def __init__(self, text, questionId):
            self.text = text
            self.id = questionId
            self.answers = []

        def addAnswer(self, answer: AnswerTemp):
            self.answers.append(answer)

    class PollTemp:
        def __init__(self, name, pollId):
            self.id = pollId
            self.name = name
            self.questions = dict()

        def addQuestion(self, question: QuestionTemp):
            if question.id in self.questions:
                return
            self.questions[question.id] = question

    class Stats:
        def __init__(self):
            self.polls = dict()

        def addPoll(self, poll: PollTemp):
            if poll.id in self.polls:
                return
            self.polls[poll.id] = poll

    queryset = UserAnswer.objects.filter(user=userId)
    response = Stats()
    for userAnswer in queryset:
        question = Question.objects.get(id=userAnswer.question_id)
        poll = Poll.objects.get(id=question.poll_id)

        response.addPoll(PollTemp(poll.name, poll.id))
        response.polls[poll.id].addQuestion(QuestionTemp(question.text, question.id))

        if userAnswer.type == 0:
            response.polls[poll.id].questions[question.id].addAnswer(AnswerTemp(userAnswer.stringAns))
        elif userAnswer.type == 1:
            answer = Answer.objects.get(id=int(userAnswer.stringAns))
            response.polls[poll.id].questions[question.id].addAnswer(AnswerTemp(answer.text, answer.id))
        elif userAnswer.type == 2:
            for answerId in userAnswer.stringAns.split(','):
                answer = Answer.objects.get(id=int(answerId))
                response.polls[poll.id].questions[question.id].addAnswer(AnswerTemp(answer.text, answer.id))

    return json.dumps(response, sort_keys=True, indent=4, default=lambda o: o.__dict__)
