"""empty message

Revision ID: 99cd2a081a3c
Revises: 8ec8c7bb9459
Create Date: 2018-11-05 17:25:39.127962

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '99cd2a081a3c'
down_revision = '8ec8c7bb9459'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account_notes', 'by_account_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account_notes', 'by_account_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###
