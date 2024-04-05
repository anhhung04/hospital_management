from tests import TestIntegration, gen_name, gen_username, gen_ssn


class TestPatient(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/patient"

    def test_list_patient(self):
        for i in range(5):
            self.test_create_patient()
        res = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 5
        })
        data = res.json()['data']
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data), 5)

    def test_get_patient_by_id(self):
        res = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        })
        data = res.json()['data']
        patient_id = data[0]['id']
        res = self._s.get(self.path(f"/{patient_id}"))
        print(res.json())
        print(res.json()['data'])
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['personal_info']["id"], patient_id)

    def test_create_patient(self):
        first_name, last_name = gen_name()
        res = self._s.post(self.path('/create'), json={
            "first_name":        first_name,
            "last_name":        last_name,
            "birth_date":       "2004-05-06",
            "gender":           "male",
            "ssn":              gen_ssn(),
            "phone_number":     "0123456789",
            "email":            gen_username() + "@user.com",
            "health_insurance": "99999999999",
            "address":          "268 ly thuong kiet"
        })
        print(res.json()['message'])
        self.assertEqual(res.status_code, 200)
        print(res.json()['data'])
        self.assertIsNotNone(res.json()['data']['username'])
        self.assertIsNotNone(res.json()['data']['password'])
        self.assertIsNotNone(res.json()['data']['user_id'])

    def test_update_patient(self):
        res = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        })
        print(res.json())
        data = res.json()['data']
        patient_id = data[0]['id']
        res = self._s.patch(self.path(f"/update/{patient_id}"), json={
            "personal_info": {
                "first_name":        "new first name",
                "last_name":        "new last name",
                "birth_date":       "2004-05-06",
            }
        })
        print(res.json())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json()['data']['personal_info']["first_name"], "new first name")
        self.assertEqual(
            res.json()['data']['personal_info']["last_name"], "new last name")
        self.assertEqual(res.json()['data']['personal_info']["id"], patient_id)
