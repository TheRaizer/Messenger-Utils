"""change user password_hash data type

Revision ID: 7853f5e7004f
Revises: 618a9abaab80
Create Date: 2022-11-06 03:19:31.307624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7853f5e7004f'
down_revision = '618a9abaab80'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('user', 'password_hash', type_=sa.VARCHAR(100), existing_nullable=False)


def downgrade() -> None:
    op.alter_column('user', 'password_hash', type_=sa.CHAR(60), existing_nullable=False)
