from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.views import MenuItemViewSet
from django.urls import reverse

class MenuItemViewSetTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Meatball', price=7.50, inventory=10)
        Menu.objects.create(title='Cheese cake', price=4.00, inventory=4)
    
    def test_getall(self):
        client = Client()
        response = client.get(reverse('menu'))
        queryset = Menu.objects.all()

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.data, queryset)
