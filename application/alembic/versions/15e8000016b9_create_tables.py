"""create tables

Revision ID: 15e8000016b9
Revises: 
Create Date: 2024-06-22 17:50:14.408864

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "15e8000016b9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.LargeBinary(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "habits",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name_habit", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("habit_goal", sa.String(), nullable=False),
        sa.Column("user", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "habittrackings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("alert_time", sa.DateTime(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("habit", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["habit"],
            ["habits.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("habit"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("habittrackings")
    op.drop_table("habits")
    op.drop_table("users")
    # ### end Alembic commands ###