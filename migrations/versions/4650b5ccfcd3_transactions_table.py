"""transactions table

Revision ID: 4650b5ccfcd3
Revises: 861a02dbced0
Create Date: 2018-09-23 20:22:35.019482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4650b5ccfcd3'
down_revision = '861a02dbced0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_due_date'), 'transaction', ['due_date'], unique=False)
    op.create_index(op.f('ix_transaction_timestamp'), 'transaction', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_timestamp'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_due_date'), table_name='transaction')
    op.drop_table('transaction')
    # ### end Alembic commands ###
