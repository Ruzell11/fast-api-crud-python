"""change email and password length

Revision ID: 4f372c3283a4
Revises: 54ad93986d19
Create Date: 2023-08-02 09:36:40.213954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f372c3283a4'
down_revision = '54ad93986d19'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("users" , "password" , type=sa.String(255))
    op.alter_column("users" , "email" , type=sa.String(255))


def downgrade() -> None:
   op.alter_column("users" , "password" , type=sa.String(50))
   op.alter_column("users" , "email" , type=sa.String(50))
