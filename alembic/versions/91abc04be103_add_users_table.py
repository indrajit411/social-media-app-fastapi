"""add users table

Revision ID: 91abc04be103
Revises: 3af23c69c906
Create Date: 2022-07-30 15:29:12.377026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "91abc04be103"
down_revision = "3af23c69c906"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
