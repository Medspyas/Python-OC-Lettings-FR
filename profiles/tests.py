from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class ProfilesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="dan", password='1234')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_index_view(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profiles')

    def test_profile_detail_view(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Paris')