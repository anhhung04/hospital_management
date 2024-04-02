"""add user and relevant table

Revision ID: 9a3655547f18
Revises: fb499768fa17
Create Date: 2024-04-02 19:55:28.208422+07:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9a3655547f18'
down_revision: Union[str, None] = 'fb499768fa17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_index('ix_patient_progresses_id', table_name='patient_progresses')
    op.drop_table('patient_progresses')
    op.drop_index('ix_medical_records_id', table_name='medical_records')
    op.drop_table('medical_records')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_ssn', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_table('employees')
    # ### end Alembic commands ###


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('ssn', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('health_insurance', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('nation', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('province', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('role', postgresql.ENUM('PATIENT', 'EMPLOYEE', 'ADMIN', name='userrole'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_ssn', 'users', ['ssn'], unique=True)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('employees',
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('employee_type', postgresql.ENUM('DOCTOR', 'NURSE', 'MANAGER', name='employeetype'), autoincrement=False, nullable=True),
    sa.Column('education_level', postgresql.ENUM('BACHELOR', 'MASTER', 'DOCTOR', 'UNDERGRADUATE', 'UNKNOWN', name='educatelevel'), autoincrement=False, nullable=True),
    sa.Column('begin_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('faculty', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='employees_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', name='employees_pkey')
    )
    op.create_table('patients',
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='patients_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', name='patients_pkey')
    )

    op.create_table('medical_records',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('medical_records_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.user_id'], name='medical_records_patient_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='medical_records_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_medical_records_id', 'medical_records', ['id'], unique=False)
    op.create_table('patient_progresses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('treatment_schedule', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('treatment_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('patient_condition', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('patient_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('medical_record_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['medical_record_id'], ['medical_records.id'], name='patient_progresses_medical_record_id_fkey'),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.user_id'], name='patient_progresses_patient_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='patient_progresses_pkey')
    )
    op.create_index('ix_patient_progresses_id', 'patient_progresses', ['id'], unique=False)
    
    # ### end Alembic commands ###
