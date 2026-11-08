"""Create organization, user and RBAC foundation."""
from alembic import op
import sqlalchemy as sa
revision = "0001_identity"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table("organizations", sa.Column("id", sa.Uuid(), primary_key=True), sa.Column("name", sa.String(160), nullable=False), sa.Column("slug", sa.String(80), nullable=False, unique=True), sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()))
    op.create_table("users", sa.Column("id", sa.Uuid(), primary_key=True), sa.Column("organization_id", sa.Uuid(), sa.ForeignKey("organizations.id", ondelete="RESTRICT")), sa.Column("email", sa.String(254), nullable=False), sa.Column("full_name", sa.String(160), nullable=False), sa.Column("password_hash", sa.String(255), nullable=False), sa.Column("is_platform_superuser", sa.Boolean(), nullable=False, server_default=sa.false()), sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()), sa.Column("is_verified", sa.Boolean(), nullable=False, server_default=sa.false()), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()))
    op.create_index("ix_users_org_email", "users", ["organization_id", "email"], unique=True)
    op.create_table("roles", sa.Column("id", sa.Uuid(), primary_key=True), sa.Column("organization_id", sa.Uuid(), sa.ForeignKey("organizations.id", ondelete="CASCADE")), sa.Column("name", sa.String(80), nullable=False), sa.Column("description", sa.String(255)), sa.Column("is_system_role", sa.Boolean(), nullable=False, server_default=sa.false()), sa.UniqueConstraint("organization_id", "name", name="uq_roles_org_name"))
    op.create_table("permissions", sa.Column("id", sa.Uuid(), primary_key=True), sa.Column("code", sa.String(120), nullable=False, unique=True), sa.Column("description", sa.String(255), nullable=False))
    op.create_table("user_roles", sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True), sa.Column("role_id", sa.Uuid(), sa.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True), sa.UniqueConstraint("user_id", "role_id", name="uq_user_roles_user_role"))
    op.create_table("role_permissions", sa.Column("role_id", sa.Uuid(), sa.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True), sa.Column("permission_id", sa.Uuid(), sa.ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True), sa.UniqueConstraint("role_id", "permission_id", name="uq_role_permissions_pair"))

def downgrade() -> None:
    op.drop_table("role_permissions")
    op.drop_table("user_roles")
    op.drop_table("permissions")
    op.drop_table("roles")
    op.drop_index("ix_users_org_email", table_name="users")
    op.drop_table("users")
    op.drop_table("organizations")
