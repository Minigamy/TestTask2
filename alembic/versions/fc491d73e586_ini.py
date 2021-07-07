"""ini

Revision ID: fc491d73e586
Revises: 6ba1e084f040
Create Date: 2021-07-05 17:43:39.630504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc491d73e586'
down_revision = '6ba1e084f040'
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
