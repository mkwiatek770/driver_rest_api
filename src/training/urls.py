from django.urls import path, include
from rest_framework import routers
from training.views import TrainingViewSet, QuestionViewSet, AnswerViewSet

router = routers.SimpleRouter()
router.register(r'training', TrainingViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
