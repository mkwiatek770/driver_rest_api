from rest_framework import serializers
from advice.models import Advice, WeekAdvice


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    # def __repr__(self):
    #     import pdb
    #     pdb.set_trace()
    media = serializers.FilePathField(path="/home/flush")

    class Meta:
        fields = "__all__"
        model = Advice


class WeekAdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = WeekAdvice
