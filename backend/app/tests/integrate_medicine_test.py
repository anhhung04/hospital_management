from tests import TestIntegration, gen_ssn, gen_username, gen_name

class TestMedicine(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/medicine"

    def test_create_employee(self):
        first_name, last_name = gen_name()
        path = self._base + "/employee/create"
        response = self._s.post(path, json={
            "first_name":         first_name,
            "last_name":          last_name,
            "birth_date":         "2004-05-06",
            "gender":             "Nữ",
            "ssn":                gen_ssn(),
            "phone_number":       "0123456789",
            "email":              gen_username() + "@user.com",
            "health_insurance":    "11111111111",
            "address":            "268 ly thuong kiet",
            "employee_type":      "OTHER",
        })
        username = response.json()['data']['username']
        password = response.json()['data']['password']
        return username, password

    def test_list_medicines(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })

        for _ in range(5):
            self.test_create_medicine()
        response = self._s.get(self.path("/list"), params={
            "page": 1,
            "limit": 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 5)

    def test_get_medicine(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })

        medicine_id = self.test_create_medicine()
        response = self._s.get(self.path(f"/{medicine_id}"))
        self.assertEqual(response.status_code, 200)

    def test_create_medicine(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })

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
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })
      
        medicine_id = self.test_create_medicine()
        for _ in range(5):
            response = self._s.post(self.path(f"/{medicine_id}/batch/create"), json={
                "import_date": "2024-05-06",
                "expiration_date": "2024-05-30",
                "quantity": 2,
                "price": 2,
                "price_per_unit": 1,
                "manufacturer": "test",
                "details": "test"
            })
        response = self._s.get(self.path(f"/{medicine_id}/batch/list"), params={
            "page": 1,
            "limit": 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 5)

    def test_get_batch(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })        

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
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        username, password = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })        

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