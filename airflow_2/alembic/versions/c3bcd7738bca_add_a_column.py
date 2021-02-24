"""add a column

Revision ID: c3bcd7738bca
Revises: 
Create Date: 2021-02-08 10:19:06.960589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3bcd7738bca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('', sa.Column('GE_validation_result'))
    pass


def downgrade():
    pass
