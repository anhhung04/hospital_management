from sqlalchemy import String, Integer, Date, ForeignKey, Column, Table
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship
from repository.schemas import Base, ObjectID
from enum import Enum

class ContainerType(Enum):
    MEDICINE = 'MEDICINE'
    EQUIPMENT = 'EQUIPMENT'

# employee_manage_container = Table(
#     "in_charge_of_containers", Base.metadata,
#     Column("employee_id", ObjectID, ForeignKey("employees.user_id")),
#     Column("container_id", ObjectID, ForeignKey("containers.id")),
#     Column("action", String, default=""),
#     extend_existing=True
# )

class Container(Base):
    __tablename__ = 'containers'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    import_date = mapped_column(Date)
    import_quantity = mapped_column(Integer)
    details = mapped_column(String)
    container_type = mapped_column(DBEnum(ContainerType))
    container_price = mapped_column(Integer)
    price_per_unit = mapped_column(Integer)
    manufacturer = mapped_column(String)

    __mapper_args__ = {
        'polymorphic_on': container_type
    }

class MedicineBatch(Container):
    __tablename__ = 'medicine_batches'
    expiration_date = mapped_column(Date)
    id = mapped_column(ForeignKey('containers.id'), primary_key=True)
    medicine_id = mapped_column(ForeignKey('medicines.id'))
    medicine = relationship("Medicine", back_populates="batches")

    __mapper_args__ = {
        'polymorphic_identity': ContainerType.MEDICINE
    }

class EquipmentBatch(Container):
    __tablename__ = 'equipment_batches'
    id = mapped_column(ForeignKey('containers.id'), primary_key=True)
    equipment_id = mapped_column(ForeignKey('equipments.id'))
    equipment = relationship("Equipment", back_populates="batches")

    __mapper_args__ = {
        'polymorphic_identity': ContainerType.EQUIPMENT
    }

# medical_instruction = Table(
#     "medical_instructions", Base.metadata,
#     Column("medicine_id", ObjectID, ForeignKey("medicines.id")),
#     Column("prescription_id", ObjectID, ForeignKey("prescriptions.id")),
#     Column("quantity", Integer, default=1),
#     Column("instruction", String, default=""),
#     extend_existing=True
# )

class Medicine(Base):
    __tablename__ = 'medicines'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    name = mapped_column(String)
    description = mapped_column(String)
    quantity = mapped_column(Integer)
    batches = relationship("MedicineBatch", back_populates="medicine")

class Equipment(Base):
    __tablename__ = 'equipments'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    name = mapped_column(String)
    availability = mapped_column(Integer)
    maintanance_history = mapped_column(String)
    batches = relationship("EquipmentBatch", back_populates="equipment")
