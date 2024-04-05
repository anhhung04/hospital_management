"""alter schema

Revision ID: 7ea72d83ee82
Revises: 4ea90dc70b62
Create Date: 2024-04-04 08:12:10.973771+07:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ea72d83ee82'
down_revision: Union[str, None] = '4ea90dc70b62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('in_charge_of_patients',
                    sa.Column('employee_id', sa.VARCHAR(), nullable=True),
                    sa.Column('progress_id', sa.Integer(), nullable=True),
                    sa.Column('action', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['employee_id'], ['employees.user_id'], ),
                    sa.ForeignKeyConstraint(
                        ['progress_id'], ['patient_progresses.id'], )
                    )
    op.drop_constraint('employees_user_id_key', 'employees', type_='unique')
    op.add_column('patient_progresses', sa.Column(
        'duration', sa.Integer(), nullable=True))
    op.execute("""
        CREATE TYPE progressstatus AS ENUM ('SCHEDULING', 'PROCESSING', 'FINISHED');
    """)
    op.add_column('patient_progresses', sa.Column(
        'status', sa.Enum('SCHEDULING', 'PROCESSING', 'FINISHED', name='progressstatus'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient_progresses', 'status')
    op.drop_column('patient_progresses', 'duration')
    op.create_unique_constraint(
        'employees_user_id_key', 'employees', ['user_id'])
    op.drop_table('in_charge_of_patients')
    # ### end Alembic commands ###
