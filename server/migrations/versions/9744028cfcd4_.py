"""empty message

Revision ID: 9744028cfcd4
Revises: c9208f26ab0a
Create Date: 2023-07-01 17:31:07.839029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9744028cfcd4'
down_revision = 'c9208f26ab0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('birds', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('birds', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
