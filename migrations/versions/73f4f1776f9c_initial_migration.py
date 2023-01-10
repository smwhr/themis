"""Initial migration.

Revision ID: 73f4f1776f9c
Revises: 
Create Date: 2022-12-28 14:24:10.456703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73f4f1776f9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('communaute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personne',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('nom', sa.String(length=255), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.Column('prenom', sa.String(length=255), nullable=True),
    sa.Column('communaute_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('compte',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=255), nullable=True),
    sa.Column('personne_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('compte_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('montant', sa.Integer(), nullable=True),
    sa.Column('libelle', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('compte')
    op.drop_table('personne')
    op.drop_table('communaute')
    # ### end Alembic commands ###