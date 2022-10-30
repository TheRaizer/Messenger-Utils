"""rename specifierId to specifier_id in FriendshipStatusSchema

Revision ID: f190687a3407
Revises: 2cd8c3fa9311
Create Date: 2022-10-29 23:48:38.185318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f190687a3407'
down_revision = '2cd8c3fa9311'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # the existing params are required for mysql
    op.alter_column('friendship_status', 'specifierId', existing_type=sa.Integer, existing_nullable=False, new_column_name='specifier_id')


def downgrade() -> None:
    op.alter_column('friendship_status', 'specifier_id', existing_type=sa.Integer, existing_nullable=False, new_column_name='specifierId')
