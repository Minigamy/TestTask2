"""ini

Revision ID: d63d3b09f7cf
Revises: fc491d73e586
Create Date: 2021-07-05 23:17:06.111660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd63d3b09f7cf'
down_revision = 'fc491d73e586'
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