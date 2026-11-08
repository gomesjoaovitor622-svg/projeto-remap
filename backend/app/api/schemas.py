from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=256)
    organization_slug: str | None = Field(default=None, min_length=1, max_length=80)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    organization_id: UUID | None
    email: EmailStr
    full_name: str
    is_platform_superuser: bool
    is_active: bool
