from tests import TestIntegration, gen_name, gen_username, gen_ssn


class TestMedicalRecord(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/medical_record"

    def test_get_self_medical_record(self):
        first_name, last_name = gen_name()
        res = self._s.post(self._base + "/patient/create", json={
            "first_name":        first_name,
            "last_name":        last_name,
            "birth_date":       "2004-05-06",
            "ssn":              gen_ssn(),
            "phone_number":     "0123456789",
            "email":            gen_username() + "@user.com",
            "health_insurance": "99999999999",
            "address":          "268 ly thuong kiet",
            "gender":           "male"
        })
        username = res.json()['data']['username']
        password = res.json()['data']['password']
        patient_id = res.json()['data']['user_id']
        res = self._s.post(self.path("/create"), json={
            "patient_id": patient_id,
            "weight": 50.5,
            "height": 1.7,
            "note": "note",
            "current_treatment": "treatment",
            "drug_allergies": "drug",
            "food_allergies": "food",
            "medical_history": "history"
        }).json()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        access_token = res.json()['data']['access_token']
        self._s.headers.update({"Authorization": f"Bearer {access_token}"})
        res = self._s.get(self.path("/me"))
        print(res.json())
        self.assertEqual(res.status_code, 200)
