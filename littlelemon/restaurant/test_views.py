from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import MenuItems
from .serializers import MenuItemsSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItems.objects.create(title="Pho", price=10, inventory=50)
        MenuItems.objects.create(title="Bun bo Hue", price=10, inventory=50)

    def test_getall(self):
        url = reverse('MenuItemView')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menuItems = MenuItems.objects.all()
        menuItemsSerializer = MenuItemsSerializer(menuItems, many=True)
        self.assertEqual(menuItemsSerializer.data, response.data)