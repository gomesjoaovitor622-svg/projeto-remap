from app.models import Organization, Permission, Role, RolePermission, User, UserRole

def test_identity_models_are_registered_in_metadata() -> None:
    expected = {"organizations", "users", "roles", "permissions", "user_roles", "role_permissions"}
    assert expected.issubset(set(Organization.metadata.tables))
    assert User.__tablename__ == "users"
    assert Role.__tablename__ == "roles"
    assert Permission.__tablename__ == "permissions"
    assert UserRole.__tablename__ == "user_roles"
    assert RolePermission.__tablename__ == "role_permissions"

def test_platform_superuser_is_explicit_and_org_is_optional() -> None:
    columns = User.__table__.columns
    assert columns["is_platform_superuser"].nullable is False
    assert columns["organization_id"].nullable is True
