from tests import gen_name, gen_username, gen_ssn, TestIntegration

class TestEmployee(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/employee"

    def test_list_employee(self):
        for _ in range(5):
            self.test_create_employee()
        response = self._s.get(self.path('/list'), params={
            "type": "all",
            "page": 5,
            "employee_per_page": 5
        })
        data = response.json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_create_employee(self):
        first_name, last_name = gen_name()
        response = self._s.post(self.path('/create'), json={
            "first_name":         first_name,
            "last_name":          last_name,
            "birth_date":         "2004-05-06",
            "gender":             "female",
            "ssn":                gen_ssn(),
            "phone_number":       "0123456789",
            "email":              gen_username() + "@user.com",
            "health_insurance":    "11111111111",
            "address":            "268 ly thuong kiet",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['data']['username'])
        self.assertIsNotNone(response.json()['data']['password'])
        self.assertIsNotNone(response.json()['data']['user_id'])
        username = response.json()['data']['username']
        password = response.json()['data']['password']
        employee_id = response.json()['data']['user_id']
        return username, password, employee_id
    
    def test_get_employee_by_id(self):
        response = self._s.get(self.path('/list'), params={
            "type": "all",
            "page": 1,
            "employee_per_page": 1
        })
        data = response.json()['data']
        employee_id = data[0]['id']
        self.assertEqual(response.status_code, 200)

    def test_update_employee(self):
        response = self._s.get(self.path('/list'), params={
            "type": "all",
            "page": 1,
            "employee_per_page": 1
        })
        data = response.json()['data']
        employee_id = data[0]['id']
        first_name, last_name = gen_name()
        new_first_name = f"new {first_name}"
        new_last_name = f"new {last_name}"
        response = self._s.patch(self.path(f"/{employee_id}/update"), json={
            "personal_info": {
                "first_name": new_first_name,
                "last_name": new_last_name,
                "birth_date": "2004-05-06",   
            },
            "employee_type": "doctor"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['personal_info']['first_name'], new_first_name)
        self.assertEqual(response.json()['data']['personal_info']['last_name'], new_last_name)
        self.assertEqual(response.json()['data']['personal_info']['id'], employee_id)
        self.assertEqual(response.json()['data']['employee_type'], "doctor")
        