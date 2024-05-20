from tests import TestIntegration, gen_id, gen_name, gen_ssn, gen_username
import random

class TestCalendar(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/employee"
        self.frequency = ['DAILY', 'WEEKLY', 'MONTHLY', 'YEARLY']

    def test_list_events(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        self.test_create_recurring_event(random.choice(self.frequency))
        response = self._s.get(self.path(f"/{employee_id}/event/list"), params={
            "begin_date": "2024-04-19",
            "end_date": "2024-04-19"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()['data']), dict)
        self.assertIsNotNone(response.json()['data']['2024-04-19'])

    def test_list_events_fail(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.get(self.path(f"/{employee_id}/event/list"), params={
            "begin_date": "2024-04-19",
            "end_date": "2024-04-18"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], "Begin date must be less than or equal end date")

    def test_create_recurring_event(self, frequency: str = "DAILY"):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.post(self.path(f"/{employee_id}/event/create"), json={
            "title": "string",
            "day_of_week": "MONDAY",
            "begin_time": "03:35:59",
            "end_time": "05:35:59",
            "begin_date": "2024-04-19",
            "is_recurring": True,
            # "end_date": "2024-04-19",
            "frequency": frequency
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['title'], "string")
        self.assertEqual(data['day_of_week'], "MONDAY")
        self.assertEqual(data['begin_time'], "03:35")
        self.assertEqual(data['end_time'], "05:35") 
        self.assertEqual(data['begin_date'], "2024-04-19")
        self.assertEqual(data['is_recurring'], True)
        # self.assertEqual(data['end_date'], "2024-04-19")
        self.assertEqual(data['frequency'], frequency)
        return data['id']

    def test_create_single_event(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.post(self.path(f"/{employee_id}/event/create"), json={
            "title": "string",
            "day_of_week": "MONDAY",
            "begin_time": "03:35:59",
            "end_time": "05:35:59",
            "begin_date": "2024-04-19",
            "is_recurring": False,
            # "end_date": "2024-04-19",
            "frequency": "SINGLE"
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['title'], "string")
        self.assertEqual(data['day_of_week'], "MONDAY")
        self.assertEqual(data['begin_time'], "03:35")
        self.assertEqual(data['end_time'], "05:35") 
        self.assertEqual(data['begin_date'], "2024-04-19")
        self.assertEqual(data['is_recurring'], False)
        self.assertEqual(data['end_date'], "2024-04-19")
        self.assertEqual(data['frequency'], "SINGLE")
        return data['id']

    def test_create_event_fail(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        response = self._s.post(self.path(f"/{employee_id}/event/create"), json={
            "title": "string",
            "day_of_week": "MONDAY",
            "begin_time": "03:35:59",
            "end_time": "05:35:59",
            "begin_date": "2024-04-19",
            "is_recurring": True,
            "frequency": "SINGLE"
        })
        self.assertEqual(response.status_code, 500)

        response = self._s.post(self.path(f"/{employee_id}/event/create"), json={ 
            "day_of_week": "MONDAY",
            "begin_time": "03:35:59",
            "end_time": "05:35:59",
            "begin_date": "2024-04-19",
            "is_recurring": False,
            "frequency": random.choice(self.frequency)
        })
        self.assertEqual(response.status_code, 500)

        response = self._s.post(self.path(f"/{employee_id}/event/create"), json={
            "title": "string",
            "day_of_week": "MONDAY",
            "begin_time": "03:35:59",
            "end_time": "02:35:59",
            "begin_date": "2024-04-19",
            "is_recurring": False,
            "frequency": "SINGLE"
        })
        self.assertEqual(response.status_code, 500)

    def test_get_event(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        event_id = self.test_create_recurring_event(random.choice(self.frequency))
        response = self._s.get(self.path(f"/{employee_id}/event/{event_id}"))
        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['id'], event_id)
        self.assertIsNotNone(data['title'])
        self.assertIsNotNone(data['day_of_week'])
        self.assertIsNotNone(data['begin_time'])
        self.assertIsNotNone(data['end_time'])
        self.assertIsNotNone(data['begin_date'])
        self.assertIsNotNone(data['is_recurring'])
        self.assertIsNotNone(data['frequency'])

    def test_self_get_event_fail(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        event_id = gen_id()
        response = self._s.get(self.path(f"/{employee_id}/event/{event_id}"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], "Event not found")

    def test_update_event(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        event_id = self.test_create_recurring_event(random.choice(self.frequency))
        response = self._s.patch(self.path(f"/{employee_id}/event/{event_id}/update"), json={
            "title": "string",
            "begin_time": "03:35:59",
            "end_time": "04:35:59",
            "end_date": "2024-04-20",
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['id'], event_id)
        self.assertEqual(data['title'], "string")
        self.assertEqual(data['begin_time'], "03:35")
        self.assertEqual(data['end_time'], "04:35") 
        self.assertEqual(data['is_recurring'], True)
        self.assertEqual(data['end_date'], "2024-04-20")

    def test_update_event_fail(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        event_id = self.test_create_recurring_event(random.choice(self.frequency))
        response = self._s.patch(self.path(f"/{employee_id}/event/{event_id}/update"), json={
            "title": "string",
            "begin_time": "03:35:59",
            "end_time": "01:35:59",
            "end_date": "2024-04-20",
        })
        self.assertEqual(response.status_code, 500)

    def test_delete_event(self):
        employee_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        event_id = self.test_create_single_event()
        response = self._s.delete(self.path(f"/{employee_id}/event/{event_id}/delete"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Event deleted successfully")

    def test_no_permission(self):
        event_id = self.test_create_recurring_event(random.choice(self.frequency))
        another_id = "189a8780-98f2-45de-8522-a048b36beb9e"
        username, password, _ = self.test_create_employee()
        res = self._s.post(self._base + "/auth/login", json={
            "username": username,
            "password": password
        })
        self._access_token = res.json()['data']['access_token']
        self._s.headers.update({
            "Authorization": f"Bearer {self._access_token}"
        })

        response = self._s.get(self.path(f"/{another_id}/event/list"))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied") 

        response = self._s.get(self.path(f"/{another_id}/event/{event_id}"))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied")

        response = self._s.patch(self.path(f"/{another_id}/event/{event_id}/update"), json={
            "title": "string",
            "begin_time": "03:35:59",
            "end_time": "04:35:59",
            "end_date": "2024-04-20",
        })
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied")

        response = self._s.delete(self.path(f"/{another_id}/event/{event_id}/delete"))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['message'], "Permission denied")

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


        
    

    