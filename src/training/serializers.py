from rest_framework.serializers import HyperlinkedModelSerializer
from training.models import Training, Question, Answer


class TrainingSerializer(HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Training


class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question


class AnswerSerializer(HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer
