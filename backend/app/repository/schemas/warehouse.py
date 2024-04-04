from sqlalchemy import String, Integer, Date, ForeignKey, Column, Table
from sqlalchemy import Enum as DBEnum
from sqlalchemy.orm import mapped_column, relationship
from repository.schemas import Base, ObjectID
from enum import Enum

class ContainerType(Enum):
    MEDICINE = 'medicine'
    EQUIPMENT = 'equipment'

class Container(Base):
    __tablename__ = 'containers'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    import_date = mapped_column(Date)
    export_date = mapped_column(Date)
    import_quantity = mapped_column(Integer)
    remaining_quantity = mapped_column(Integer)
    expiration_date = mapped_column(Date)
    details = mapped_column(String)
    container_type = mapped_column(DBEnum(ContainerType))
    container_price = mapped_column(Integer)
    price_per_unit = mapped_column(Integer)
    manufacturer = mapped_column(String)

class Medicine(Base):
    __tablename__ = 'medicines'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    container_id = mapped_column(ForeignKey('containers.id'))
    medicine_name = mapped_column(String)
    container_info = relationship("Container", primaryjoin="Medicine.container_id == Container.id")

medical_instruction = Table(
    "medical_instructions", Base.metadata,
    Column("medicine_id", ObjectID, ForeignKey("medicines.id")),
    Column("prescription_id", ObjectID, ForeignKey("prescriptions.id")),
    Column("quantity", Integer, default=1),
    Column("instruction", String, default=""),
    extend_existing=True
)

class Equipment(Base):
    __tablename__ = 'equipments'

    id = mapped_column(ObjectID, primary_key=True, index=True)
    container_id = mapped_column(ForeignKey('containers.id'))
    name = mapped_column(String)
    availability = mapped_column(Integer)
    maintanance_history = mapped_column(String)
    container_info = relationship("Container", primaryjoin="Equipment.container_id == Container.id")

employee_manage_container = Table(
    "in_charge_of_containers", Base.metadata,
    Column("employee_id", ObjectID, ForeignKey("employees.user_id")),
    Column("container_id", ObjectID, ForeignKey("containers.id")),
    Column("action", String, default=""),
    extend_existing=True
)
