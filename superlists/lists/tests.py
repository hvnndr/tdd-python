from django.http import HttpRequest
from django.test import TestCase
from . import views
from django.urls import resolve


class HomePagetest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = views.home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)



# run with python manage.py test
