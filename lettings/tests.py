from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting



class LettingsViewsTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Main street',
            city='Miami',
            state='Florida',
            zip_code=98210,
            country_iso_code='USA',
        )

        self.letting = Letting.objects.create(
            title='House',
            address=self.address
        )
    def test_lettings_index_view(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'House')

    def test_lettings_detail_view(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Main street')
