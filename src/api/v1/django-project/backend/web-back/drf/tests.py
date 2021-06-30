from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Drf


class DrfModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Drf.objects.create(title="first drf", body="a body here")

    def test_title_content(self):
        drf = Drf.objects.get(id=1)
        excepted_object_name = f'{drf.title}'
        self.assertEqual(excepted_object_name, 'first drf')

    def test_body_content(self):
        drf = Drf.objects.get(id=1)
        excepted_object_name = f'{drf.body}'
        self.assertEqual(excepted_object_name, 'a body here')
