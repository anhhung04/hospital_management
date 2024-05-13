# from unittest import TestCase
# from tests import override_get_db, insert_patient
# from repository.schemas.patient import Patient, MedicalRecord, PatientProgress, ProgressType, Conclusion, TestResult, Prescription, EmployeeHandlePatient
# from datetime import datetime, date

# class PatientTest(TestCase):
#     def test_insert_patient(self):
#         db = next(override_get_db())
#         user_id = "123"
#         p = insert_patient(db, user_id)
#         p_n_db = db.query(Patient).filter(Patient.user_id == p.user_id).first()
#         self.assertTrue(p_n_db is not None)
#         self.assertTrue(p_n_db.user_id == p.user_id)

#         # Test MedicalRecord
#         mr = MedicalRecord(weight=70, height=170, note="Test note", current_treatment="Test treatment", drug_allergies="None", food_allergies="None", medical_history="None")
#         db.add(mr)
#         db.commit()
#         mr_n_db = db.query(MedicalRecord).filter(MedicalRecord.id == mr.id).first()
#         self.assertTrue(mr_n_db is not None)
#         self.assertTrue(mr_n_db.weight == mr.weight)
#         self.assertTrue(mr_n_db.height == mr.height)
#         self.assertTrue(mr_n_db.note == mr.note)
#         self.assertTrue(mr_n_db.current_treatment == mr.current_treatment)
#         self.assertTrue(mr_n_db.drug_allergies == mr.drug_allergies)
#         self.assertTrue(mr_n_db.food_allergies == mr.food_allergies)
#         self.assertTrue(mr_n_db.medical_history == mr.medical_history)

#         # Test PatientProgress
#         pp = PatientProgress(id = "1", start_treatment=datetime.now(), end_treatment=datetime.now(), patient_condition="Test condition", patient_id=p.user_id, status=ProgressType.SCHEDULING, medical_record_id=mr.id)
#         db.add(pp)
#         db.commit()
#         pp_n_db = db.query(PatientProgress).filter(PatientProgress.id == pp.id).first()
#         self.assertTrue(pp_n_db is not None)
#         self.assertTrue(pp_n_db.start_treatment == pp.start_treatment)
#         self.assertTrue(pp_n_db.end_treatment == pp.end_treatment)
#         self.assertTrue(pp_n_db.patient_condition == pp.patient_condition)
#         self.assertTrue(pp_n_db.patient_id == pp.patient_id)
#         self.assertTrue(pp_n_db.status == pp.status)
#         self.assertTrue(pp_n_db.medical_record_id == pp.medical_record_id)

#         # Test Conclusion
#         c = Conclusion(id = "1", diagnosis="Test diagnosis", advice="Test advice", prescription_id=1)
#         db.add(c)
#         db.commit()
#         c_n_db = db.query(Conclusion).filter(Conclusion.id == c.id).first()
#         self.assertTrue(c_n_db is not None)
#         self.assertTrue(c_n_db.diagnosis == c.diagnosis)
#         self.assertTrue(c_n_db.advice == c.advice)
#         self.assertTrue(c_n_db.prescription_id == c.prescription_id)

#         # Test TestResult
#         now = datetime.now()
#         datenow = date.today()
#         tr = TestResult(id = "1", created_at = now, result_date = datenow, test_type = "Test type", details = "Test details", medical_record_id = mr.id)
#         db.add(tr)
#         db.commit()
#         tr_n_db = db.query(TestResult).filter(TestResult.id == tr.id).first()
#         self.assertTrue(tr_n_db is not None)
#         self.assertTrue(tr_n_db.created_at == tr.created_at)
#         self.assertTrue(tr_n_db.result_date == tr.result_date)
#         self.assertTrue(tr_n_db.test_type == tr.test_type)
#         self.assertTrue(tr_n_db.details == tr.details)
#         self.assertTrue(tr_n_db.medical_record_id == tr.medical_record_id)

#         # Test Prescription
#         p = Prescription(id = "1", note = "Test note", progress_id = pp.id)
#         db.add(p)
#         db.commit()
#         p_n_db = db.query(Prescription).filter(Prescription.id == p.id).first()
#         self.assertTrue(p_n_db is not None)
#         self.assertTrue(p_n_db.note == p.note)
#         self.assertTrue(p_n_db.progress_id == p.progress_id)

#         # Test Employee handle patient
#         ehp = EmployeeHandlePatient(employee_id="1", progress_id="1", action="Test action")
#         db.add(ehp)
#         db.commit()
#         ehp_n_db = db.query(EmployeeHandlePatient).filter(EmployeeHandlePatient.employee_id == ehp.employee_id).first()
#         self.assertTrue(ehp_n_db is not None)
#         self.assertTrue(ehp_n_db.progress_id == ehp.progress_id)
#         self.assertTrue(ehp_n_db.action == ehp.action)
#         db.close()
    