from tests import TestIntegration


class TestMetric(TestIntegration):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._route = "/metric"

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
