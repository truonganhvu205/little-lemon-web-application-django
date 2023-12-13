from django.test import TestCase
from restaurant.models import MenuItems

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")