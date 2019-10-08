from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from training.serializers import TrainingSerializer, QuestionSerializer, AnswerSerializer
from training.models import Training, Question, Answer
# Create your views here.


class TrainingViewSet(ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
