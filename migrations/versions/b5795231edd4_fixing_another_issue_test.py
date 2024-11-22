"""fixing another issue test

Revision ID: b5795231edd4
Revises: e14d5170df65
Create Date: 2024-11-18 16:21:24.357339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5795231edd4'
down_revision = 'e14d5170df65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coordinates', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('batteryId')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coordinates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('batteryId', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'batteries', ['batteryId'], ['id'])

    # ### end Alembic commands ###
