import unittest
import requests
from models.inventory import InventoryModel


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"

    expected_result = {
        "id": 48,
        "name": "Jeans",
        "category": "Clothings",
        "manufacturing_date": "02-02-2022, 00:24:00",
        "expiry_date": "11-21-2021, 02:37:21",
        "quantity": 222,
        "file": "C:/Users/agbha/PycharmProjects/Assignment-3/inventory/image11111111.png",
        "timezone": "America/Chicago"
    }

    updated_data = {
        "id": 48,
        "name": "Jeans",
        "category": "Clothings",
        "manufacturing_date": "02-02-2022, 00:24:00",
        "expiry_date": "11-21-2021, 02:37:21",
        "quantity": 222,
        "file": "C:/Users/agbha/PycharmProjects/Assignment-3/inventory/image11111111.png",
        "timezone": "America/Chicago"
    }

    def test_for_get_all_data(self):
        resp = requests.get(self.URL + 'inventory-list')
        self.assertEqual(resp.status_code, 200)
        print("Test 1 Completed.")

    def test_get_data_by_name(self):
        resp = requests.get(self.URL + 'inventory/Jeans')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), self.expected_result)
        print("Test 2 Completed.")

    def test_for_post_data(self):
        resp = requests.post(self.URL + "Jeans", json=self.expected_result)
        self.assertEqual(resp.status_code, 200)
        print("Test 3 Completed.")
    #
    def test_for_delete_data(self):
        resp = requests.delete(self.URL + 'inventory/Trouser')
        self.assertEqual(resp.status_code, 200)
        print("Test 4 Completed.")

    def test_for_update_data(self):
        resp = requests.put(self.URL + 'inventory/Shirts', json=self.updated_data)
        self.assertEqual(resp.json()['id'], self.updated_data['id'])
        self.assertEqual(resp.json()['name'], self.updated_data['name'])
        self.assertEqual(resp.json()['category'], self.updated_data['category'])
        self.assertEqual(resp.json()['manufacturing_date'], self.updated_data['manufacturing_date'])
        self.assertEqual(resp.json()['expiry_date'], self.updated_data['expiry_date'])
        self.assertEqual(resp.json()['quantity'], self.updated_data['quantity'])
        print("Test 5 Completed.")


if __name__ == '__main__':
    tester = TestAPI()

    test_for_get_all_data()
    test_get_data_by_name()
    test_for_post_data()
    test_for_delete_data()
    test_for_update_data()
