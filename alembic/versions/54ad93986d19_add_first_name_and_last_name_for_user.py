"""add first name and last name for user

Revision ID: 54ad93986d19
Revises: 5fbdc94bcaff
Create Date: 2023-07-31 14:04:43.522666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54ad93986d19'
down_revision = '5fbdc94bcaff'
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.add_column('users' , sa.Column('first_name' , sa.String(length=255), nullable=False))
   op.add_column('users' , sa.Column('last_name' , sa.String(length=255), nullable=False))


def downgrade() -> None:
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
