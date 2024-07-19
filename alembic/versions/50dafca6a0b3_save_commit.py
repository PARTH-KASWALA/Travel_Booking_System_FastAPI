"""save commit

Revision ID: 50dafca6a0b3
Revises: 4fa08d9c3574
Create Date: 2024-07-19 15:29:09.865121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50dafca6a0b3'
down_revision: Union[str, None] = '4fa08d9c3574'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('booking_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.String(length=50), nullable=False),
    sa.Column('payment_status', sa.String(length=50), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('transaction_id', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['bookings.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('bookings', sa.Column('payment_id', sa.String(length=100), nullable=True))
    op.create_foreign_key(None, 'bookings', 'payment', ['payment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bookings', type_='foreignkey')
    op.drop_column('bookings', 'payment_id')
    op.drop_table('payment')
    # ### end Alembic commands ###