from datetime import datetime, timedelta, timezone
from uuid import UUID
import jwt
from pwdlib import PasswordHash
from app.core.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    try:
        return password_hash.verify(password, hashed)
    except Exception:
        return False

def create_access_token(*, user_id: UUID, organization_id: UUID | None) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": str(user_id), "org": str(organization_id) if organization_id else None, "iat": now, "exp": now + timedelta(minutes=settings.access_token_minutes), "type": "access"}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm], options={"require": ["sub", "exp", "iat", "type"]})
