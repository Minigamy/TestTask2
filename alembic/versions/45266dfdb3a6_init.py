"""init

Revision ID: 45266dfdb3a6
Revises: 
Create Date: 2021-07-05 16:45:54.056928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45266dfdb3a6'
down_revision = None
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
