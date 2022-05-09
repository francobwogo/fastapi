"""Create posts table

Revision ID: d17e3c1f5553
Revises: 
Create Date: 2022-05-09 16:26:58.721702

"""
from tokenize import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd17e3c1f5553'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
