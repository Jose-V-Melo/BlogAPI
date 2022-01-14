"""create post table

Revision ID: a6378ba1012e
Revises: 5b1d1e864aee
Create Date: 2022-01-13 20:18:08.009623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6378ba1012e'
down_revision = '5b1d1e864aee'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("created_date", sa.DATETIME),
        sa.Column("title", sa.String(100)),
        sa.Column("body", sa.String(1000)),
        sa.Column("owner_id", sa.Integer),
        sa.Column("is_active", sa.Boolean)
    )


def downgrade():
    op.drop_table("users")
