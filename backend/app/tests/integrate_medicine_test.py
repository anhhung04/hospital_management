from tests import TestIntegration, gen_id, gen_name, gen_ssn, gen_username
import random

class TestMedicine(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/medicine"

    def test_list_medicines(self):
        response = self._s.get(self.path("/list"))
        self.assertEqual(response.status_code, 200)

    def test_get_medicine(self):
        medicine_id = self.test_create_medicine()
        response = self._s.get(self.path(f"/{medicine_id}"))
        self.assertEqual(response.status_code, 200)

    def test_create_medicine(self):
        response = self._s.post(self.path("/create"), json={
            "name": "panadol",
            "description": "HDSD",
            "quantity": 10
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['name'], "panadol")
        self.assertEqual(response.json()['data']['description'], "HDSD")
        self.assertEqual(response.json()['data']['quantity'], 10)
        return response.json()['data']['id']
    
    def test_list_batches(self):
        medicine_id = self.test_create_medicine()
        response = self._s.get(self.path(f"/{medicine_id}/batch/list"))
        self.assertEqual(response.status_code, 200)

        response = self._s.post(self.path(f"/{medicine_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "expiration_date": "2024-05-30",
            "quantity": 2,
            "price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })
        self.assertEqual(response.status_code, 200)
        response = self._s.get(self.path(f"/{medicine_id}/batch/list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 1)


    def test_get_batch(self):
        medicine_id = self.test_create_medicine()
        response = self._s.post(self.path(f"/{medicine_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "expiration_date": "2024-05-30",
            "quantity": 2,
            "price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })
        batch_id = response.json()['data']['id']  
        response = self._s.get(self.path(f"/{medicine_id}/batch/{batch_id}"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['id'], batch_id)


    def test_create_batch(self):
        medicine_id = self.test_create_medicine()
        response = self._s.post(self.path(f"/{medicine_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "expiration_date": "2024-05-30",
            "quantity": 2,
            "price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['quantity'], 2)
        self.assertEqual(response.json()['data']['price'], 2)
        self.assertEqual(response.json()['data']['price_per_unit'], 1)
        self.assertEqual(response.json()['data']['manufacturer'], "test")
        self.assertEqual(response.json()['data']['details'], "test")
        self.assertEqual(response.json()['data']['import_date'], "2024-05-06")  
        self.assertEqual(response.json()['data']['expiration_date'], "2024-05-30")
        return response.json()['data']['id']