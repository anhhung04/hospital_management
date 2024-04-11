"""seed employee

Revision ID: ae8e99277c90
Revises: 9a3655547f18
Create Date: 2024-04-02 20:10:44.426666+07:00

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ae8e99277c90'
down_revision: Union[str, None] = '9a3655547f18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
        CREATE EXTENSION pgcrypto;
        INSERT INTO users (id, ssn, phone_number, birth_date, gender, health_insurance, last_name, first_name, address, email, username, password, role) VALUES 
        ('189a8780-98f2-45de-8522-a048b36beb9e', '123456789', '0123456789', '2000-01-01', 'male', '123456789', 'Nguyễn Văn', 'A', '268 Ly Thuong Kiet', 'nguyenvana@gmail.com', 'employee1', '18124aeeecee69daf749c1d96bc0eacc331c78f520533180fbf14fce0824450a', 'employee:employeetype.manager'),
        ('289a8780-98f2-45de-8522-a048b36beb9e', '123456780', '0123456780', '2000-01-01', 'female', '123456780', 'Nguyễn Thị', 'B', '268 Ly Thuong Kiet', 'nguyenvanb@gmail.com', 'employee2', 'de08da8c83b62313f3cb789d6fd46fa2621b71113a754ecf8f422504ac977f94', 'employee'),
        ('389a8780-98f2-45de-8522-a048b36beb9e', '123456780', '0123456780', '2004-01-01', 'mail', '123456780', 'AB', 'C', '268 Ly Thuong Kiet', 'abc@gmail.com', 'adminuser', 'ad247b7d865c22c8b7974ce86ae7e1ff47f807f074f454dde3657515dbc17e4b', 'employee');
        
        INSERT INTO employees (user_id, employee_type, education_level, begin_date, end_date, faculty) VALUES
        ('189a8780-98f2-45de-8522-a048b36beb9e', 'MANAGER', 'UNKNOWN', '2020-01-01', '2024-12-01', 'Back Khoa University'),
        ('289a8780-98f2-45de-8522-a048b36beb9e', 'DOCTOR', 'BACHELOR', '2020-01-01', '2024-12-01', 'Back Khoa University');
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass
