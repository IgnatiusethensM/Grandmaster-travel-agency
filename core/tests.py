from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class RememberMeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()

    def test_remember_me_checked(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123',
            'remember_me': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        
        # Check session expiry
        session = self.client.session
        self.assertEqual(session.get_expiry_age(), 1209600)  # 2 weeks

    def test_remember_me_unchecked(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
            # remember_me missing or off
        })
        self.assertEqual(response.status_code, 302)
        
        # Check session expiry
        session = self.client.session
        self.assertTrue(session.get_expire_at_browser_close())
