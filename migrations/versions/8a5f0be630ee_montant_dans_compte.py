"""Montant dans compte

Revision ID: 8a5f0be630ee
Revises: 73f4f1776f9c
Create Date: 2023-01-11 13:08:53.190167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5f0be630ee'
down_revision = '73f4f1776f9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('compte', schema=None) as batch_op:
        batch_op.add_column(sa.Column('montant', sa.Integer(), server_default='0', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('compte', schema=None) as batch_op:
        batch_op.drop_column('montant')

    # ### end Alembic commands ###
