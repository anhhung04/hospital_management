from tests import TestIntegration

class TestEquipment(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/equipment"
    
    def test_list_equipments(self):
        response = self._s.get(self.path("/list"))
        self.assertEqual(response.status_code, 200)

    def test_get_equipment(self):
        equipment_id = self.test_create_equipment()
        response = self._s.get(self.path(f"/{equipment_id}"))
        self.assertEqual(response.status_code, 200)

    def test_create_equipment(self):
        response = self._s.post(self.path("/create"), json={
            "name": "laptop",
            "description": "HDSD",
            "quantity": 1,
            "status": "Good",
            "availability": True,
            "maintanance_history": "test"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['name'], "laptop")
        self.assertEqual(response.json()['data']['description'], "HDSD")
        self.assertEqual(response.json()['data']['quantity'], 1)
        self.assertEqual(response.json()['data']['status'], "Good")
        self.assertEqual(response.json()['data']['availability'], True)
        self.assertEqual(response.json()['data']['maintanance_history'], "test")
        return response.json()['data']['id']
    
    def test_list_batches(self):
        equipment_id = self.test_create_equipment()
        response = self._s.get(self.path(f"/{equipment_id}/batch/list"))
        self.assertEqual(response.status_code, 200)

        response = self._s.post(self.path(f"/{equipment_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "import_quantity": 2,
            "container_price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })
        self.assertEqual(response.status_code, 200)
        response = self._s.get(self.path(f"/{equipment_id}/batch/list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 1)

    def test_get_batch(self):
        equipment_id = self.test_create_equipment()
        response = self._s.post(self.path(f"/{equipment_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "import_quantity": 2,
            "container_price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })
        batch_id = response.json()['data']['id']
        response = self._s.get(self.path(f"/{equipment_id}/batch/{batch_id}"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['id'], batch_id)

    def test_create_batch(self):
        equipment_id = self.test_create_equipment()
        response = self._s.post(self.path(f"/{equipment_id}/batch/create"), json={
            "import_date": "2024-05-06",
            "import_quantity": 2,
            "container_price": 2,
            "price_per_unit": 1,
            "manufacturer": "test",
            "details": "test"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['import_quantity'], 2)
        self.assertEqual(response.json()['data']['container_price'], 2)
        self.assertEqual(response.json()['data']['price_per_unit'], 1)
        self.assertEqual(response.json()['data']['manufacturer'], "test")
        self.assertEqual(response.json()['data']['details'], "test")
        self.assertEqual(response.json()['data']['import_date'], "2024-05-06")
        return response.json()['data']['id']