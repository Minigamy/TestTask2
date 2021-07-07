"""init

Revision ID: 6ba1e084f040
Revises: 45266dfdb3a6
Create Date: 2021-07-05 17:33:45.585786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ba1e084f040'
down_revision = '45266dfdb3a6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'anagram',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('count', sa.Integer)
    )


def downgrade():
    op.deop_table('anagram')
