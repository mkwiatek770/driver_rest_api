from django.urls import path, include
from rest_framework import routers
from advice.views import AdviceViewSet, WeekAdviceViewSet

router = routers.SimpleRouter()
router.register(r'advice', AdviceViewSet)
router.register(r'week-advice', WeekAdviceViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
