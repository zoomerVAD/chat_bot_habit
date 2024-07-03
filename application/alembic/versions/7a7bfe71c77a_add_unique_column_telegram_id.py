"""add unique column telegram_id

Revision ID: 7a7bfe71c77a
Revises: 15e8000016b9
Create Date: 2024-07-03 00:24:42.969698

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7a7bfe71c77a"
down_revision: Union[str, None] = "15e8000016b9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "users", ["telegram_id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    # ### end Alembic commands ###
