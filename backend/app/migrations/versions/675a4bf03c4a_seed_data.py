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
        ('980b8598-c4f7-4ad4-8736-609be91b1934', '123456784', '0123456784', '1982-01-01', 'male', '123456784', 'Nguyễn Như', 'Thủy', '268 Ngo Quyen', 'nguyennthuy@gmail.com', 'nguyennthuy', '39ed8a74a7b7331a3c905bb86d159fcafe55357e35ba26e2b1e84e2497516ae5', 'employee:employeetype.doctor'),
        ('f643133d-0a99-4a7d-9cdd-b771de636a84', '123456785', '0123456785', '1990-01-01', 'female', '123456785', 'Lê Thị', 'Mỹ', '219 Ly Thuong Kiet', 'lethimy@gmail.com', 'lethimy', '4816e13b44e3ee87fa1d8621eea50a8ba15aeb6811853c08073389cc801fd14e', 'employee:employeetype.nurse'),
        ('fd158827-8813-4be5-8983-cc5f1dd1e8d6', '123456786', '0123456786', '1998-01-01', 'male', '123456786', 'Ngô Văn', 'Tùng', '8 Nguyen Tri Phuong', 'ngovantung@gmail.com', 'ngovantung', '4cf168fb27a67d81f04c796d0c573007496c943e3f94d02b2845cc7a87bde557', 'employee:employeetype.manager'),
        ('b6113e94-e0bb-4b69-81cb-cbf9863981db', '123456787', '0123456787', '1992-01-01', 'female', '123456787', 'Hoàng Thị', 'Châu', '28 Au Co', 'hoangthichau@gmail.com', 'hoangthichau', 'd643d59c62801419e8c97b7b414bd3c524fecb6f8c5b8016a54a79353ff8d992', 'employee:employeetype.other'),
        ('3b8c457a-9cb9-4e54-bc4e-0ad7e818b349', '123456788', '0123456788', '1993-01-01', 'male', '123456788', 'Châu Văn', 'Bảo', '293 Hoang Sa', 'chauvanbao@gmail.com', 'chauvanbao', '37fb7ae0d50c0aa6d1a46be14a5a1d4deae95fa5896933b8e673e67d5c86e94f', 'employee:employeetype.doctor'),
        ('c5af7fd2-0eaf-4da0-8cf3-15b3619112b1', '123456778', '0123456789', '1982-01-01', 'female', '123456789', 'Lê Thị', 'Tiên', '232 Truong Sa', 'lttien@gmail.com', 'lttien', 'f2167e4b1296bec9383438131827af5d600acbb29e713cc18b7ee000b90f6628', 'employee:employeetype.nurse'),
        ('330393df-2378-4a4e-a74c-51880dfd19a4', '123456792', '0123456780', '1978-01-01', 'male', '123456780', 'Nguyễn Văn', 'An', '103 Ngo Quyen', 'ngvanan@gmail.com', 'ngvanan', '77c54b124036df04e7cc5e8a3cc449a26dcf21047fc77f76f482e804fd273abb', 'employee:employeetype.manager'),
        ('382d1947-71d1-4533-964d-22daa2a99c40', '123456781', '0123456781', '1980-01-01', 'female', '123456781', 'Nguyễn Thị', 'Sương', '8 Hung Vuong', 'nguyenvans@gmail.com', 'nguyenvans', 'a4423e2b5b1dd6a688a56fa6c8b01d926639b051e4aff9137b3d18ebaca9d23e', 'employee:employeetype.other'),
        ('c0f498d2-842d-4fca-9f04-eb1f7e045503', '123456782', '0123456782', '1989-01-01', 'male', '123456782', 'Trương Đức', 'Hào', '26 Ho Dac Di', 'trgduchao@gmail.com', 'trgduchao', 'ae89b83133b3ccfa3639942cb0a819065cdd547e33a84d1af8612bb73b3a4678', 'employee:employeetype.doctor'),
        ('d89a8780-98f2-45de-8522-a048b36beb9e', '123456765', '0123456783', '2000-01-01', 'female', '123456783', 'Nguyễn Thị', 'Như', '92 Ly Thuong Kiet', 'nguyenthinhu@gmail.com', 'nguyenthinhu', '304b5ccb5fdcee1eb3075374f386844ad9c2793e197bd35644af3b941a6e3d9a', 'employee:employeetype.nurse');
        
        INSERT INTO employees (user_id, employee_type, education_level, begin_date, end_date, faculty) VALUES
        ('980b8598-c4f7-4ad4-8736-609be91b1934', 'DOCTOR', 'MASTER', '2020-01-01', '2024-12-01', 'Anesthetics'),
        ('f643133d-0a99-4a7d-9cdd-b771de636a84', 'NURSE', 'BACHELOR', '2020-01-01', '2024-12-01', 'Breast Screening'),
        ('fd158827-8813-4be5-8983-cc5f1dd1e8d6', 'MANAGER', 'MASTER', '2020-01-01', '2024-12-01', 'Cardiology'),
        ('b6113e94-e0bb-4b69-81cb-cbf9863981db', 'OTHER', 'UNDERGRADUATE', '2020-01-01', '2024-12-01', 'Elderly Services'),
        ('3b8c457a-9cb9-4e54-bc4e-0ad7e818b349', 'DOCTOR', 'MASTER', '2020-01-01', '2024-12-01', 'Critical Care'),
        ('c5af7fd2-0eaf-4da0-8cf3-15b3619112b1', 'NURSE', 'DOCTOR', '2020-01-01', '2024-12-01', 'General Services'),
        ('330393df-2378-4a4e-a74c-51880dfd19a4', 'MANAGER', 'MASTER', '2020-01-01', '2024-12-01', 'General Surgery'),
        ('382d1947-71d1-4533-964d-22daa2a99c40', 'MANAGER', 'BACHELOR', '2020-01-01', '2024-12-01', 'Hematology'),
        ('c0f498d2-842d-4fca-9f04-eb1f7e045502', 'OTHER', 'UNKNOWN', '2020-01-01', '2024-12-01', 'Health & Safety'),
        ('d89a8780-98f2-45de-8522-a048b36beb9e', 'NURSE', 'DOCTOR', '2020-01-01', '2024-12-01', 'Neurology');
    """)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass

