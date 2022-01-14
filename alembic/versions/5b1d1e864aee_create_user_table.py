"""create user table

Revision ID: 5b1d1e864aee
Revises: 
Create Date: 2022-01-13 00:29:00.320076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1d1e864aee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("created_date", sa.DATETIME),
        sa.Column("email", sa.String(200)),
        sa.Column("username", sa.String(100), unique=True),
        sa.Column("hashed_password", sa.String(100)),
        sa.Column("is_active", sa.Boolean)
    )


def downgrade():
    op.drop_table("users")
