"""Create tables productions

Revision ID: 453bdb5c931c
Revises: 
Create Date: 2024-04-23 10:46:54.277090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '453bdb5c931c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('composer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productions')
    # ### end Alembic commands ###
