"""empty message

Revision ID: d58d1159149e
Revises: ba6e4bc83cc1
Create Date: 2016-03-06 11:35:16.153000

"""

# revision identifiers, used by Alembic.
revision = 'd58d1159149e'
down_revision = 'ba6e4bc83cc1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('last_changed', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_feedback_last_changed'), 'feedback', ['last_changed'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feedback_last_changed'), table_name='feedback')
    op.drop_column('feedback', 'last_changed')
    ### end Alembic commands ###