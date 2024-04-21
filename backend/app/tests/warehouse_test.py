from datetime import date
from unittest import TestCase
from tests import override_get_db
from repository.schemas.warehouse import Container, Medicine, Equipment, ContainerType, employee_manage_container, medical_instruction

class WarehouseTest(TestCase):
    def test_insert_container(self):
        db = next(override_get_db())
        c = Container(id = "1",import_date=date.today(), export_date=date.today(), import_quantity=100, remaining_quantity=100, expiration_date=date.today(), details="Test details", container_type=ContainerType.MEDICINE, container_price=100, price_per_unit=1, manufacturer="Test manufacturer")
        db.add(c)
        db.commit()
        c_n_db = db.query(Container).filter(Container.id == c.id).first()
        self.assertTrue(c_n_db is not None)
        self.assertTrue(c_n_db.import_date == c.import_date)
        self.assertTrue(c_n_db.export_date == c.export_date)
        self.assertTrue(c_n_db.import_quantity == c.import_quantity)
        self.assertTrue(c_n_db.remaining_quantity == c.remaining_quantity)
        self.assertTrue(c_n_db.expiration_date == c.expiration_date)
        self.assertTrue(c_n_db.details == c.details)
        self.assertTrue(c_n_db.container_type == c.container_type)
        self.assertTrue(c_n_db.container_price == c.container_price)
        self.assertTrue(c_n_db.price_per_unit == c.price_per_unit)
        self.assertTrue(c_n_db.manufacturer == c.manufacturer)

    def test_insert_medicine(self):
        db = next(override_get_db())
        m = Medicine(id = "1", container_id="1", medicine_name="Test medicine", container_info=None)
        db.add(m)
        db.commit()
        m_n_db = db.query(Medicine).filter(Medicine.id == m.id).first()
        self.assertTrue(m_n_db is not None)
        self.assertTrue(m_n_db.container_id == m.container_id)
        self.assertTrue(m_n_db.medicine_name == m.medicine_name)
        self.assertTrue(m_n_db.container_info == m.container_info)

    def test_insert_equipment(self):
        db = next(override_get_db())
        e = Equipment(id = "1", container_id="1", name="Test equipment", availability=100, maintanance_history="Test history", container_info=None)
        db.add(e)
        db.commit()
        e_n_db = db.query(Equipment).filter(Equipment.id == e.id).first()
        self.assertTrue(e_n_db is not None)
        self.assertTrue(e_n_db.container_id == e.container_id)
        self.assertTrue(e_n_db.name == e.name)
        self.assertTrue(e_n_db.availability == e.availability)
        self.assertTrue(e_n_db.maintanance_history == e.maintanance_history)
        self.assertTrue(e_n_db.container_info == e.container_info)

    def test_insert_employee_manage_container(self):
        db = next(override_get_db())
        db.execute(employee_manage_container.insert().values(employee_id="123", container_id="1", action="Test action"))
        db.commit()
        emc = db.query(employee_manage_container).filter(employee_manage_container.c.employee_id == "123").first()
        self.assertTrue(emc is not None)
        self.assertTrue(emc.employee_id == "123")
        self.assertTrue(emc.container_id == "1")
        self.assertTrue(emc.action == "Test action")
        
    def test_insert_medical_instruction(self):
        db = next(override_get_db())
        db.execute(medical_instruction.insert().values(medicine_id="123", prescription_id="1", quantity=1, instruction="Test instruction"))
        db.commit()
        mi = db.query(medical_instruction).filter(medical_instruction.c.prescription_id == "1").first()
        self.assertTrue(mi is not None)
        self.assertTrue(mi.prescription_id == "1")
        self.assertTrue(mi.medicine_id == "123")
        self.assertTrue(mi.quantity == 1)
        self.assertTrue(mi.instruction == "Test instruction")
