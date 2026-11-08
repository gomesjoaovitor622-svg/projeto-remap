from types import SimpleNamespace
from uuid import uuid4
from unittest.mock import MagicMock
import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from app.api.deps import get_current_user, require_platform_superuser
from app.core.security import create_access_token, decode_access_token, hash_password, verify_password
from app.models import User

def test_password_hash_verifies_without_storing_plaintext():
    raw = "Correct-Horse-Battery-2026!"
    hashed = hash_password(raw)
    assert raw not in hashed
    assert verify_password(raw, hashed)
    assert not verify_password("wrong-password", hashed)

def test_access_token_contains_user_and_tenant_scope():
    user_id, org_id = uuid4(), uuid4()
    payload = decode_access_token(create_access_token(user_id=user_id, organization_id=org_id))
    assert payload["sub"] == str(user_id)
    assert payload["org"] == str(org_id)
    assert payload["type"] == "access"

def test_user_cannot_use_token_for_another_organization():
    org_a, org_b, user_id = uuid4(), uuid4(), uuid4()
    token = create_access_token(user_id=user_id, organization_id=org_a)
    user = SimpleNamespace(id=user_id, organization_id=org_b, is_active=True)
    db = MagicMock()
    db.get.return_value = user
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)
    with pytest.raises(HTTPException) as exc:
        get_current_user(credentials=credentials, db=db)
    assert exc.value.status_code == 401

def test_inactive_organization_cannot_authenticate():
    org_id, user_id = uuid4(), uuid4()
    token = create_access_token(user_id=user_id, organization_id=org_id)
    user = SimpleNamespace(id=user_id, organization_id=org_id, is_active=True)
    db = MagicMock()
    db.get.side_effect = [user, SimpleNamespace(id=org_id, is_active=False)]
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)
    with pytest.raises(HTTPException) as exc:
        get_current_user(credentials=credentials, db=db)
    assert exc.value.status_code == 401

def test_only_platform_superuser_passes_global_guard():
    regular = SimpleNamespace(is_platform_superuser=False)
    with pytest.raises(HTTPException) as exc:
        require_platform_superuser(user=regular)
    assert exc.value.status_code == 403
