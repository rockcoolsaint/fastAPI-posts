"""add content column to posts table

Revision ID: 4a34e1b2c0aa
Revises: dc3a8bef7c07
Create Date: 2023-09-27 19:13:40.407389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4a34e1b2c0aa"
down_revision: Union[str, None] = "dc3a8bef7c07"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
