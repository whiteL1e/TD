from django.test import TestCase
from django.urls import resolve
from lists.views import home_page   # (2)

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')    # (1)
        self.assertEqual(found.func, home_page) # (1)

# **************1*****************
# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

# Create your tests here.
