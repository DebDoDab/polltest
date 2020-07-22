from django.http import Http404, HttpResponse
from polls.models import Answer, Poll, Question, UserAnswer
import json


def get_statistics(user_id):
    """Get all answered questions for given user"""
    class AnswerTemp:
        def __init__(self, text, answer_id=None):
            self.id = answer_id
            self.text = text

    class QuestionTemp:
        def __init__(self, text, question_id):
            self.text = text
            self.id = question_id
            self.answers = []

        def add_answer(self, answer: AnswerTemp):
            self.answers.append(answer)

    class PollTemp:
        def __init__(self, name, poll_id):
            self.id = poll_id
            self.name = name
            self.questions = dict()

        def add_question(self, question: QuestionTemp):
            if question.id in self.questions:
                return
            self.questions[question.id] = question

    class Stats:
        def __init__(self):
            self.polls = dict()

        def add_poll(self, poll: PollTemp):
            if poll.id in self.polls:
                return
            self.polls[poll.id] = poll

    queryset = UserAnswer.objects.filter(user=user_id)
    response = Stats()
    for userAnswer in queryset:
        question = Question.objects.get(id=userAnswer.question_id)
        poll = Poll.objects.get(id=question.poll_id)

        response.add_poll(PollTemp(poll.name, poll.id))
        response.polls[poll.id].addQuestion(QuestionTemp(question.text, question.id))

        if userAnswer.type == 0:
            response.polls[poll.id].questions[question.id].add_answer(AnswerTemp(userAnswer.string_ans))
        elif userAnswer.type == 1:
            answer = Answer.objects.get(id=int(userAnswer.string_ans))
            response.polls[poll.id].questions[question.id].add_answer(AnswerTemp(answer.text, answer.id))
        elif userAnswer.type == 2:
            for answer_id in userAnswer.stringAns.split(','):
                answer = Answer.objects.get(id=int(answer_id))
                response.polls[poll.id].questions[question.id].add_answer(AnswerTemp(answer.text, answer.id))

    return json.dumps(response, sort_keys=True, indent=4, default=lambda o: o.__dict__)
