"""add model relation

Revision ID: 8b26acb52712
Revises: 86ab65acccac
Create Date: 2023-11-06 20:22:53.555408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b26acb52712'
down_revision = '86ab65acccac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'category', ['category'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category')

    # ### end Alembic commands ###