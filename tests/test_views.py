
from rest_framework.test import APITestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
class MenuViewTest(APITestCase):
    def setUp(self):
        Menu.objects.create(Title="Pizza", Price=12, Inventory=10)
        Menu.objects.create(Title="Pasta", Price=10, Inventory=8)
        Menu.objects.create(Title="Salad", Price=5, Inventory=15)

    def test_get_all(self):
        items=Menu.objects.all()
        serializer=MenuSerializer(items,many=True)

        response=self.client.get('/restaurant/menu/', HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,serializer.data)