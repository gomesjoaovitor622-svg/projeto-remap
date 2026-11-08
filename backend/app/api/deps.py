from collections.abc import Generator
from uuid import UUID
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.db.session import SessionLocal
from app.models import Organization, User

bearer = HTTPBearer(auto_error=False)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(bearer), db: Session = Depends(get_db)) -> User:
    unauthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas.", headers={"WWW-Authenticate": "Bearer"})
    if credentials is None:
        raise unauthorized
    try:
        payload = decode_access_token(credentials.credentials)
        user_id = UUID(payload["sub"])
        organization_id = UUID(payload["org"]) if payload.get("org") else None
    except (jwt.PyJWTError, ValueError, KeyError):
        raise unauthorized
    user = db.get(User, user_id)
    if user is None or not user.is_active or user.organization_id != organization_id:
        raise unauthorized
    if organization_id is not None:
        organization = db.get(Organization, organization_id)
        if organization is None or not organization.is_active:
            raise unauthorized
    return user

def require_platform_superuser(user: User = Depends(get_current_user)) -> User:
    if not user.is_platform_superuser:
        raise HTTPException(status_code=403, detail="Acesso restrito ao superusuário da plataforma.")
    return user
