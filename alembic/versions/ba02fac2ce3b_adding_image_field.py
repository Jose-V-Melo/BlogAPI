"""adding image field

Revision ID: ba02fac2ce3b
Revises: a6378ba1012e
Create Date: 2022-01-13 20:57:31.167472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba02fac2ce3b'
down_revision = 'a6378ba1012e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("url", sa.String(200))
    )


def downgrade():
    op.drop_column(
        "posts",
        "url"
    )
