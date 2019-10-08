from importlib import import_module
from rest_framework import status
from rest_framework.test import APIClient
from django.conf import settings
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, RequestFactory
from advice.models import Advice
from advice.serializers import AdviceSerializer


class TestAdviceViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_method_for_unauthenticated(self):
        response = self.client.get("http://127.0.0.1:8000/advice/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advice_detail_view(self):
        advice = self.create_advice()
        response = self.client.get(
            "http://127.0.0.1:8000/advice/{}/".format(advice.pk))
        request = init_request()
        serializer = AdviceSerializer(advice, context={"request": request})
        # import pdb
        # pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        # self.assertDictEqual(response.json(), {'url': f'http://testserver/advice/{advice.id}/', 'media': advice.media,
        #    'title': advice.title, 'description': advice.description[:-1].replace("T", " "), 'date_created': str(advice.date_created)[:-6]})

    # def test_post_method_for_unathenticated(self):
        # response = self.client.post("advice/", )

#
    # def test_post_method_for_authtenticated(self):

    def create_advice(self):
        return Advice.objects.create(
            title="some title",
            description="some description",
            media="/home/user/file.jpg"
        )


def init_request():
    """Create fake request object to use in tests"""
    request_factory = RequestFactory()
    request = request_factory.get("/")
    engine = import_module(settings.SESSION_ENGINE)
    session_key = None
    request.session = engine.SessionStore(session_key)
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)
    return request
