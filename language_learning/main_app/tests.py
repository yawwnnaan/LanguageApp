from django.test import TestCase

class SimpleTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Language Learning App")

    def test_study_page(self):
        response = self.client.get('/study/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Study Words")

    def test_test_page(self):
        response = self.client.get('/test/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Your Knowledge")