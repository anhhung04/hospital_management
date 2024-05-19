"""seed-data

Revision ID: 675a4bf03c4a
Revises: 19fdd9540637
Create Date: 2024-05-19 21:25:31.018417+07:00

"""
from typing import Sequence, Union
from alembic import op


# revision identifiers, used by Alembic.
revision: str = '675a4bf03c4a'
down_revision: Union[str, None] = '19fdd9540637'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
        INSERT INTO users (id, ssn, phone_number, birth_date, gender, health_insurance, last_name, first_name, address, email, username, password, role) VALUES 
        ('489a8780-98f2-45de-8522-a048b36beb9e', '123456784', '0123456784', '1982-01-01', 'male', '123456784', 'Nguyễn Như', 'Thủy', '268 Ngo Quyen', 'nguyennthuy@gmail.com', 'employee3', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.doctor'),
        ('589a8780-98f2-45de-8522-a048b36beb9e', '123456785', '0123456785', '1990-01-01', 'female', '123456785', 'Lê Thị', 'Mỹ', '219 Ly Thuong Kiet', 'lethimy@gmail.com', 'employee4', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.nurse'),
        ('689a8780-98f2-45de-8522-a048b36beb9e', '123456786', '0123456786', '1998-01-01', 'male', '123456786', 'Ngô Văn', 'Tùng', '8 Nguyen Tri Phuong', 'ngovantung@gmail.com', 'employee5', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.manager'),
        ('789a8780-98f2-45de-8522-a048b36beb9e', '123456787', '0123456787', '1992-01-01', 'female', '123456787', 'Hoàng Thị', 'Châu', '28 Au Co', 'hoangthichau@gmail.com', 'employee6', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.other'),
        ('889a8780-98f2-45de-8522-a048b36beb9e', '123456788', '0123456788', '1993-01-01', 'male', '123456788', 'Châu Văn', 'Bảo', '293 Hoang Sa', 'chauvanbao@gmail.com', 'employee7', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.doctor'),
        ('989a8780-98f2-45de-8522-a048b36beb9e', '123456778', '0123456789', '1982-01-01', 'female', '123456789', 'Lê Thị', 'Tiên', '232 Truong Sa', 'lttien@gmail.com', 'employee8', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.nurse'),
        ('a89a8780-98f2-45de-8522-a048b36beb9e', '123456792', '0123456780', '1978-01-01', 'male', '123456780', 'Nguyễn Văn', 'An', '103 Ngo Quyen', 'ngvanan@gmail.com', 'employee9', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.manager'),
        ('b89a8780-98f2-45de-8522-a048b36beb9e', '123456781', '0123456781', '1980-01-01', 'female', '123456781', 'Nguyễn Thị', 'Sương', '8 Hung Vuong', 'nguyenvans@gmail.com', 'employee10', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.other'),
        ('c89a8780-98f2-45de-8522-a048b36beb9e', '123456782', '0123456782', '1989-01-01', 'male', '123456782', 'Trương Đức', 'Hào', '26 Ho Dac Di', 'trgduchao@gmail.com', 'employee11', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.doctor'),
        ('d89a8780-98f2-45de-8522-a048b36beb9e', '123456765', '0123456783', '2000-01-01', 'female', '123456783', 'Nguyễn Thị', 'Như', '92 Ly Thuong Kiet', 'nguyenthinhu@gmail.com', 'employee12', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee:employeetype.nurse');
        
        INSERT INTO employees (user_id, employee_type, education_level, begin_date, end_date, faculty) VALUES
        ('489a8780-98f2-45de-8522-a048b36beb9e', 'DOCTOR', 'MASTER', '2020-01-01', '2024-12-01', 'Anesthetics'),
        ('589a8780-98f2-45de-8522-a048b36beb9e', 'NURSE', 'BACHELOR', '2020-01-01', '2024-12-01', 'Breast Screening'),
        ('689a8780-98f2-45de-8522-a048b36beb9e', 'MANAGER', 'MASTER', '2020-01-01', '2024-12-01', 'Cardiology'),
        ('789a8780-98f2-45de-8522-a048b36beb9e', 'OTHER', 'UNDERGRADUATE', '2020-01-01', '2024-12-01', 'Elderly Services'),
        ('889a8780-98f2-45de-8522-a048b36beb9e', 'DOCTOR', 'MASTER', '2020-01-01', '2024-12-01', 'Critical Care'),
        ('989a8780-98f2-45de-8522-a048b36beb9e', 'NURSE', 'DOCTOR', '2020-01-01', '2024-12-01', 'General Services'),
        ('a89a8780-98f2-45de-8522-a048b36beb9e', 'MANAGER', 'MASTER', '2020-01-01', '2024-12-01', 'General Surgery'),
        ('b89a8780-98f2-45de-8522-a048b36beb9e', 'MANAGER', 'BACHELOR', '2020-01-01', '2024-12-01', 'Hematology'),
        ('c89a8780-98f2-45de-8522-a048b36beb9e', 'OTHER', 'UNKNOWN', '2020-01-01', '2024-12-01', 'Health & Safety'),
        ('d89a8780-98f2-45de-8522-a048b36beb9e', 'NURSE', 'DOCTOR', '2020-01-01', '2024-12-01', 'Neurology');
    """)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass

