"""create comment table

Revision ID: bc59b38092fc
Revises: ba02fac2ce3b
Create Date: 2022-01-13 22:29:19.408650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc59b38092fc'
down_revision = 'ba02fac2ce3b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("created_date", sa.DATETIME),
        sa.Column("email", sa.String(200)),
        sa.Column("name", sa.String(100), unique=True),
        sa.Column("body", sa.String(1000)),
        sa.Column("post_id", sa.Integer, sa.ForeignKey("post.id")),
        sa.Column("is_active", sa.Boolean)
    )


def downgrade():
    op.drop_table("comments")
