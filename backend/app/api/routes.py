from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db, require_platform_superuser
from app.api.schemas import LoginRequest, TokenResponse, UserResponse
from app.core.security import create_access_token, verify_password
from app.models import Organization, User

router = APIRouter()

@router.post("/auth/login", response_model=TokenResponse, tags=["authentication"])
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    statement = select(User).where(User.email == payload.email.lower(), User.is_active.is_(True))
    if payload.organization_slug:
        organization = db.scalar(select(Organization).where(Organization.slug == payload.organization_slug, Organization.is_active.is_(True)))
        if organization is None:
            raise HTTPException(status_code=401, detail="E-mail, senha ou empresa inválidos.")
        statement = statement.where(User.organization_id == organization.id)
    else:
        statement = statement.where(User.organization_id.is_(None), User.is_platform_superuser.is_(True))
    user = db.scalar(statement)
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="E-mail, senha ou empresa inválidos.")
    if user.organization_id is not None and not user.is_verified:
        raise HTTPException(status_code=403, detail="Conta ainda não verificada.")
    return TokenResponse(access_token=create_access_token(user_id=user.id, organization_id=user.organization_id))

@router.get("/auth/me", response_model=UserResponse, tags=["authentication"])
def who_am_i(user: User = Depends(get_current_user)) -> User:
    return user

@router.get("/admin/platform-check", tags=["administration"])
def platform_check(user: User = Depends(require_platform_superuser)) -> dict[str, str]:
    return {"status": "authorized", "scope": "platform"}
