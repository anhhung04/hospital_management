from tests import TestIntegration, gen_name, gen_ssn, gen_username


class TestMetric(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/metric"
        self._create_patient_path = self._base + "/patient/create"
        self._create_employee_path = self._base + "/employee/create"

    def test_fetch_general(self):
        res = self._s.get(self.path('/'))
        self.assertEqual(res.status_code, 200)
        data = res.json()['data']
        self.assertIn('num_patients', data)
        self.assertIn('num_doctors', data)
        self.assertIn('num_employee', data)
        self.assertIn('patients_per_day', data)
        self.assertIsInstance(data['num_patients'], int)
        self.assertIsInstance(data['num_doctors'], int)
        self.assertIsInstance(data['num_employee'], int)
    
    def create_patient(self):
        first_name, last_name = gen_name()
        res = self._s.post(self._create_patient_path, json={
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
        patient_id = res.json()['data']['user_id']
        return patient_id
    
    def create_employee(self, type):
        first_name, last_name = gen_name()
        response = self._s.post(self._create_employee_path, json={
            "first_name":         first_name,
            "last_name":          last_name,
            "birth_date":         "2004-05-06",
            "gender":             "female",
            "ssn":                gen_ssn(),
            "phone_number":       "0123456789",
            "email":              gen_username() + "@user.com",
            "health_insurance":    "11111111111",
            "address":            "268 ly thuong kiet",
            "employee_type":      type,
        })
        employee_id = response.json()['data']['user_id']
        return employee_id
    
    def create_progress(self, patient_id):
        self._s.post(self._base + f"/patient/{patient_id}/progress/create", json={
            "start_treatment": f"2024-05-06 00:00:00",
            "end_treatment": f"2024-05-06 00:05:00",
            "patient_condition": "bad"
        })

    def test_fetch_general_logic(self):
        res = self._s.get(self.path('/'))
        data = res.json()['data']
        num_patients = data['num_patients']
        num_doctors = data['num_doctors']
        num_nurses = data['num_nurses']
        num_other = data['num_other']
        num_employees = data['num_employee']
        patients_per_day = data['patients_per_day']
        total_patients_per_day = sum(patients_per_day)
        
        for i in range (7):
            patient_id = self.create_patient()
            self.create_progress(patient_id)
            self.create_employee("DOCTOR")
            self.create_employee("NURSE")
            self.create_employee("OTHER")

            res = self._s.get(self.path('/'))
            data = res.json()['data']
            self.assertEqual(data['num_patients'], num_patients + i + 1)
            self.assertEqual(data['num_doctors'], num_doctors + i + 1)
            self.assertEqual(data['num_nurses'], num_nurses + i + 1)
            self.assertEqual(data['num_other'], num_other + i + 1)
            self.assertEqual(data['num_employee'], num_employees + 3 * i + 3)

        res = self._s.get(self.path('/'))
        data = res.json()['data']
      
        self.assertEqual(data['num_patients'], num_patients + 7)
        self.assertEqual(total_patients_per_day + 7, sum(data['patients_per_day']))
        self.assertEqual(data['num_doctors'], num_doctors + 7)
        self.assertEqual(data['num_nurses'], num_nurses + 7)
        self.assertEqual(data['num_other'], num_other + 7)
        self.assertEqual(data['num_employee'], num_employees + 21)





            

