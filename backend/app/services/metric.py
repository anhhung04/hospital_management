from repository.patient import PatientRepo
from repository.employee import EmployeeRepo
from models.metric import MetricModel
from models.employee import EmployeeType
from fastapi import Depends, HTTPException


class MetricService:
    def __init__(
        self,
        patientRepo: PatientRepo = Depends(PatientRepo),
        employeeRepo: EmployeeRepo = Depends(EmployeeRepo)
    ):
        self._patient_repo = patientRepo
        self._employee_repo = employeeRepo

    async def fetch_general(self) -> MetricModel:
        try:
            num_patients, err = await self._patient_repo.count()
            if err:
                raise err
            num_doctors, err = await self._employee_repo.count(type=EmployeeType.DOCTOR)
            if err:
                raise err
            num_employee, err = await self._employee_repo.count()
            if err:
                raise err
            patients_per_day, err = await self._patient_repo.count_per_day(7)
            if err:
                raise err
            return MetricModel(
                num_patients=num_patients,
                num_doctors=num_doctors,
                num_employee=num_employee,
                patients_per_day=patients_per_day
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
