from django.test import TestCase
from .views import signup
# Create your tests here.
class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
 .