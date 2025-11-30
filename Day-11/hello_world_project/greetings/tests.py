from django.test import TestCase, Client
from django.urls import reverse


class GreetingsViewsTestCase(TestCase):
    """Test cases for the greetings app views."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
    
    def test_home_view_status_code(self):
        """Test that home view returns 200 status code."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_template(self):
        """Test that home view uses correct template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'greetings/home.html')
    
    def test_hello_view_status_code(self):
        """Test that hello view returns 200 status code."""
        response = self.client.get(reverse('hello', kwargs={'name': 'Django'}))
        self.assertEqual(response.status_code, 200)
    
    def test_hello_view_template(self):
        """Test that hello view uses correct template."""
        response = self.client.get(reverse('hello', kwargs={'name': 'Django'}))
        self.assertTemplateUsed(response, 'greetings/hello.html')
    
    def test_hello_view_context(self):
        """Test that hello view passes name to context."""
        response = self.client.get(reverse('hello', kwargs={'name': 'World'}))
        self.assertEqual(response.context['name'], 'World')
    
    def test_hello_view_content(self):
        """Test that hello view displays the name."""
        response = self.client.get(reverse('hello', kwargs={'name': 'Student'}))
        self.assertContains(response, 'Student')
