from django.test import TestCase
from . import views
from django.urls import resolve


class HomePagetest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)


# run with python manage.py test
