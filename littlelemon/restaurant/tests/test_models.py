from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Meatball', price=7.25, inventory=15)
        self.assertEqual(item, "Meatball : 7.25")