"""add content column to posts table

Revision ID: b68e9c586b98
Revises: d17e3c1f5553
Create Date: 2022-05-09 17:44:39.790854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b68e9c586b98'
down_revision = 'd17e3c1f5553'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
