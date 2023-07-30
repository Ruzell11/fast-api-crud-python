"""create users table

Revision ID: 2e4f17d89ebd
Revises: 
Create Date: 2023-07-30 10:16:26.193341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e4f17d89ebd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id" , sa.Integer , primary_key=True),
        sa.Column("email" , sa.String(50)),
        sa.Column("password" , sa.String(50))
    )


def downgrade() -> None:
    op.drop_table('users')
