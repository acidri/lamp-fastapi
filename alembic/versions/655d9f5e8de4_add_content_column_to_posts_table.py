"""add content column to posts table

Revision ID: 655d9f5e8de4
Revises: f3c266ee2101
Create Date: 2024-05-07 14:14:22.373824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '655d9f5e8de4'
down_revision: Union[str, None] = 'f3c266ee2101'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None: 
    op.drop_column('posts', 'content')
    pass
