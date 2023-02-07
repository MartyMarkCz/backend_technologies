from django.test import TestCase
from viewer.models import *


# Create your tests here.

class ExampleTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up data for all calss method")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to set up data")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertFalse(True)

    def test_add(self):
        print("Method: test_add")
        self.assertEqual(1 + 1, 2)


class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title_orig='Test movie orig title',
            title_cz='Test movie title cz',
            title_sk='Test movie title sk',
            released=2023
        )
        country = Country.objects.create(name='CZ')
        movie.country.add(country)
        country_sk = Country.objects.create(name='SK')
        movie.country.add(country_sk)
        genre = Genre.objects.create(name='Drama')
        movie.genre.add(genre)
        movie.save()

    def test_title_orig(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title_orig, 'Test movie orig title')
