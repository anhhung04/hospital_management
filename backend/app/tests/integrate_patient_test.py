from tests import TestIntegration, gen_name, gen_username, gen_ssn
import random

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

    def test_get_own_patient(self):
        other_id = res = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        }).json()['data'][0]['id']
        res = self._s.get(self.path(f"/{other_id}"))
        self.assertEqual(res.status_code, 200)
        username, password, patient_id = self.test_create_patient()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })
        res = self._s.get(self.path(f"/{patient_id}"))
        print(res.json())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['personal_info']["id"], patient_id)
        res = self._s.get(self.path(f"/{other_id}"))
        print(res.json())
        self.assertEqual(res.status_code, 403)


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
        username = res.json()['data']['username']
        password = res.json()['data']['password']
        patient_id = res.json()['data']['user_id']
        return username, password, patient_id

    def test_update_patient(self):
        res = self._s.get(self.path('/list'), params={
            "page": 1,
            "limit": 1
        })
        print(res.json())
        data = res.json()['data']
        patient_id = data[0]['id']
        res = self._s.patch(self.path(f"/{patient_id}/update"), json={
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

    def test_add_new_progress(self):
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        print(res.json())
        self.assertEqual(res.status_code, 200)

    def test_add_invalid_progress(self):
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        self.assertEqual(res.status_code, 200)
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-03-06 00:00:00",
            "patient_condition": "good"
        })
        self.assertEqual(res.status_code, 400)

    def test_auto_process_progress(self):
        from datetime import datetime, timedelta
        _, _, patient_id = self.test_create_patient()
        current = datetime.now()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": current.__sub__(timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "end_treatment": (current := current.replace(
                month=current.month + 1)).strftime("%Y-%m-%d %H:%M:%S"),
            "patient_condition": "good"
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['status'], "PROCESSING")

    def test_view_progress(self):
        _, _, patient_id = self.test_create_patient()
        for _ in range(20):
            res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
                "start_treatment": "2024-05-06 00:00:00",
                "end_treatment": "2024-06-06 00:00:00",
                "patient_condition": "good"
            })
            print(res.json())
            self.assertEqual(res.status_code, 200)
        max_progress = random.randint(1, 8)
        res = self._s.get(self.path(f"/{patient_id}"), params={
            "page_limit": max_progress
        })
        print(res.json())
        self.assertEqual(res.status_code, 200)
        data = res.json()['data']
        self.assertEqual(len(data['medical_record']['progress']), max_progress)

    def test_update_progress(self):
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        progress_id = res.json()['data']['id']
        res = self._s.patch(self.path(f"/{patient_id}/progress/{progress_id}/update"), json={
            "lead_employee": [
                {
                    "employee_email": "nguyenvana@gmail.com",
                    "action": "do something"
                }
            ]
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['lead_employee'][0]['employee_email'], "nguyenvana@gmail.com")
        res = self._s.patch(self.path(f"/{patient_id}/progress/{progress_id}/update"), json={
            "status": "FINISHED"
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['status'], "FINISHED")

    def test_get_progress(self):
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        progress_id = res.json()['data']['id']
        self.assertEqual(res.status_code, 200)
        res = self._s.patch(self.path(f"/{patient_id}/progress/{progress_id}/update"), json={
            "lead_employee": [
                {
                    "employee_email": "nguyenvana@gmail.com",
                    "action": "do something"
                }
            ]
        })
        res = self._s.get(self.path(f"/{patient_id}/progress/{progress_id}"))
        self.assertEqual(res.status_code, 200)
        print(res.json())
        self.assertEqual(res.json()['data']['lead_employee'][0]['employee_email'], "nguyenvana@gmail.com")

    def test_progress_in_charge(self):
        res = self._s.get(self._base + "/auth/me")
        data = res.json()['data']
        doctor_id = data['id']
        doctor_email = data['email']
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        progress_id = res.json()['data']['id']
        res = self._s.patch(self.path(f"/{patient_id}/progress/{progress_id}/update"), json={
            "lead_employee": [
                {
                    "employee_email": doctor_email,
                    "action": "do something"
                }
            ]
        })
        res = self._s.get(self.path(f"/{patient_id}/progress/in-charge"), params={
            "doctor_id": doctor_id
        })
        data = res.json()
        self.assertEqual(res.status_code, 200)
        print(res.json())
        data = res.json()['data']
        print(data)
        self.assertTrue(len(data) > 0)

    def test_delete_lead_employee(self):
        _, _, patient_id = self.test_create_patient()
        res = self._s.post(self.path(f"/{patient_id}/progress/create"), json={
            "start_treatment": "2024-05-06 00:00:00",
            "end_treatment": "2024-06-06 00:00:00",
            "patient_condition": "good"
        })
        progress_id = res.json()['data']['id']
        self.assertEqual(res.status_code, 200)
        res = self._s.patch(self.path(f"/{patient_id}/progress/{progress_id}/update"), json={
            "lead_employee": [
                {
                    "employee_email": "nguyenvana@gmail.com",
                    "action": "test"
                }
            ]
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['lead_employee'][0]['employee_email'], "nguyenvana@gmail.com")
        res = self._s.delete(self.path(f"/{patient_id}/progress/{progress_id}/lead_employee"), json={
            "employee_email": "nguyenvana@gmail.com"
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['lead_employee'], [])
