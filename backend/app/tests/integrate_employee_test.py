from tests import gen_name, gen_username, gen_ssn, TestIntegration

class TestEmployee(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/employee"

    def test_list_employee(self):
        for _ in range(5):
            self.test_create_employee()
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 5
        })
        data = response.json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_list_doctor(self):
        for _ in range(5):
            self.test_create_employee()
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 5,
            "type": "DOCTOR"
        })
        print(response.json())
        data = response.json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_list_nurse(self):
        for _ in range(5):
            self.test_create_employee(type="NURSE")
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 5,
            "type": "NURSE"
        })
        print(response.json())
        data = response.json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_list_other(self):
        for _ in range(5):
            self.test_create_employee(type=None)
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 5,
            "type": "OTHER"
        })
        data = response.json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_create_employee(self, type="DOCTOR"):
        first_name, last_name = gen_name()
        response = self._s.post(self.path('/create'), json={
            "first_name":         first_name,
            "last_name":          last_name,
            "birth_date":         "2004-05-06",
            "gender":             "Nữ",
            "ssn":                gen_ssn(),
            "phone_number":       "0123456789",
            "email":              gen_username() + "@user.com",
            "health_insurance":    "11111111111",
            "address":            "268 ly thuong kiet",
            "employee_type":      type,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['data']['username'])
        self.assertIsNotNone(response.json()['data']['password'])
        self.assertIsNotNone(response.json()['data']['user_id'])
        username = response.json()['data']['username']
        password = response.json()['data']['password']
        employee_id = response.json()['data']['user_id']
        return username, password, employee_id
    
    def test_get_employee_by_id_normal_employee(self):
        username, password, employee_id = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })
        response = self._s.get(self.path(f"/{employee_id}"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['personal_info']['id'], employee_id) 

        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.get(self.path(f"/{employee_id}"))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied")
        
    def get_imployee_by_id_manager_role(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        })
        data = response.json()['data']
        employee_id = data[0]['id']

        response = self._s.get(self.path(f"/{employee_id}"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['personal_info']['id'], employee_id)

    def test_update_employee_normal_employee(self):
        username, password, employee_id = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })
        response = self._s.get(self.path(f"/{employee_id}"))
        self.assertEqual(response.status_code, 200)

        response = self._s.patch(self.path(f"/{employee_id}/update"), json={
            "begin_date": "2004-09-05",
            "end_date": "2006-09-05",
            "status": "ACTIVE",
            "education_level": "MASTER"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['begin_date'], "2004-09-05")
        self.assertEqual(response.json()['data']['end_date'], "2006-09-05")
        self.assertEqual(response.json()['data']['status'], "ACTIVE")
        self.assertEqual(response.json()['data']['personal_info']['id'], employee_id)
        self.assertEqual(response.json()['data']['education_level'], "MASTER")

        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.patch(self.path(f"/{employee_id}/update"), json={
            "begin_date": "2004-09-05",
            "end_date": "2006-09-05",
            "status": "ACTIVE",
            "education_level": "MASTER"
        })
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied")

    def test_update_employee_manager_role(self):
        self._access_token = self._s.post(self._base + "/auth/login", json={
            "username": "employee1",
            "password": "demo"
        }).json()["data"]["access_token"]
        self._s.headers = {
            "Authorization": f"Bearer {self._access_token}"
        }
        response = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        })
        data = response.json()['data']
        employee_id = data[0]['id']

        response = self._s.patch(self.path(f"/{employee_id}/update"), json={
            "begin_date": "2004-09-05",
            "end_date": "2006-09-05",
            "status": "ACTIVE",
            "education_level": "MASTER"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['begin_date'], "2004-09-05")
        self.assertEqual(response.json()['data']['end_date'], "2006-09-05")
        self.assertEqual(response.json()['data']['status'], "ACTIVE")
        self.assertEqual(response.json()['data']['personal_info']['id'], employee_id)
        self.assertEqual(response.json()['data']['education_level'], "MASTER")



        
