"""add content column to posts table

Revision ID: 1b4def1ab085
Revises: 5ee8680ade69
Create Date: 2024-04-23 21:10:05.444530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b4def1ab085'
down_revision: Union[str, None] = '5ee8680ade69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
