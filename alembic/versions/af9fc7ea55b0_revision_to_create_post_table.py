"""revision to create post table

Revision ID: af9fc7ea55b0
Revises: 
Create Date: 2022-07-30 14:05:48.967771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "af9fc7ea55b0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
