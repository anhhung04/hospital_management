"""alter medical record

Revision ID: 4ea90dc70b62
Revises: ae8e99277c90
Create Date: 2024-04-03 19:55:00.098719+07:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ea90dc70b62'
down_revision: Union[str, None] = 'ae8e99277c90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'employees', ['user_id'])
    op.add_column('medical_records', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('medical_records', sa.Column('weight', sa.Float(), nullable=True))
    op.add_column('medical_records', sa.Column('height', sa.Float(), nullable=True))
    op.add_column('medical_records', sa.Column('note', sa.String(), nullable=True))
    op.add_column('medical_records', sa.Column('current_treatment', sa.String(), nullable=True))
    op.add_column('medical_records', sa.Column('drug_allergies', sa.String(), nullable=True))
    op.add_column('medical_records', sa.Column('food_allergies', sa.String(), nullable=True))
    op.add_column('medical_records', sa.Column('medical_history', sa.String(), nullable=True))
    op.add_column('patient_progresses', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column('patient_progresses', 'date')
    op.drop_column('patients', 'height')
    op.drop_column('patients', 'note')
    op.drop_column('patients', 'weight')
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('patients', sa.Column('weight', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('patients', sa.Column('note', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('patients', sa.Column('height', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('patient_progresses', sa.Column('date', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('patient_progresses', 'created_at')
    op.drop_column('medical_records', 'medical_history')
    op.drop_column('medical_records', 'food_allergies')
    op.drop_column('medical_records', 'drug_allergies')
    op.drop_column('medical_records', 'current_treatment')
    op.drop_column('medical_records', 'note')
    op.drop_column('medical_records', 'height')
    op.drop_column('medical_records', 'weight')
    op.drop_column('medical_records', 'created_at')
    op.drop_constraint(None, 'employees', type_='unique')
    # ### end Alembic commands ###