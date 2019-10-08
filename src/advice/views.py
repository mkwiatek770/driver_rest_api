from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from advice.models import Advice, WeekAdvice
from advice.serializers import AdviceSerializer, WeekAdviceSerializer

# Create your views here.


class AdviceViewSet(ModelViewSet):
    serializer_class = AdviceSerializer
    queryset = Advice.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WeekAdviceViewSet(ModelViewSet):
    serializer_class = WeekAdviceSerializer
    queryset = WeekAdvice.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
