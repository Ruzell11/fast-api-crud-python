"""create task  table

Revision ID: 5fbdc94bcaff
Revises: 2e4f17d89ebd
Create Date: 2023-07-30 10:23:53.104060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fbdc94bcaff'
down_revision = '2e4f17d89ebd'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        "tasks",
        sa.Column("id" , sa.Integer , primary_key=True),
        sa.Column("user_id" , sa.Integer , sa.ForeignKey("users.id")),
        sa.Column("title" , sa.String(100)),
        sa.Column("description" , sa.String(100))
    )


def downgrade() -> None:
    op.drop_table("tasks")
