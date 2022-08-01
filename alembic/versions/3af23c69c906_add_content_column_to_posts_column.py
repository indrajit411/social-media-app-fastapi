"""add content column to posts column

Revision ID: 3af23c69c906
Revises: af9fc7ea55b0
Create Date: 2022-07-30 14:24:24.668470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3af23c69c906"
down_revision = "af9fc7ea55b0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
