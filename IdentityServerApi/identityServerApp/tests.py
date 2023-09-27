from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Role

class CustomUserTestCase(TestCase):
    # Test cases for CustomUser model and related functionality
 def test_user_registration(self):
    # Create a test user
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword',
        'phone_number': '1234567890',
    }
    
    response = self.client.post(reverse('signup'), user_data)
    
    # Check if the user was created successfully (HTTP 201)
    self.assertEqual(response.status_code, 201)
    
    # Check if the user exists in the database
    user_exists = CustomUser.objects.filter(username='testuser').exists()
    self.assertTrue(user_exists)





#class RoleTestCase(TestCase):
    # Test cases for Role model and related functionality
