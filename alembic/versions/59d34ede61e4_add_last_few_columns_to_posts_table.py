"""add last few columns to posts table

Revision ID: 59d34ede61e4
Revises: 4d698853b7da
Create Date: 2022-07-31 13:07:15.802170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "59d34ede61e4"
down_revision = "4d698853b7da"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
