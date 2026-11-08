import argparse
import getpass
import re
import sys
from sqlalchemy import select
from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models import User

def create_superuser() -> int:
    parser = argparse.ArgumentParser(description="Cria o primeiro superusuário global do REMAP.")
    parser.add_argument("--email", required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    email = args.email.strip().lower()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("E-mail inválido.", file=sys.stderr)
        return 2
    password = getpass.getpass("Senha forte (mínimo 12 caracteres): ")
    confirmation = getpass.getpass("Confirme a senha: ")
    if len(password) < 12 or password != confirmation:
        print("Senha curta ou confirmação diferente.", file=sys.stderr)
        return 2
    with SessionLocal() as db:
        if db.scalar(select(User.id).where(User.is_platform_superuser.is_(True)).limit(1)):
            print("Já existe um superusuário global. Operação cancelada.", file=sys.stderr)
            return 3
        if db.scalar(select(User.id).where(User.email == email, User.organization_id.is_(None))):
            print("Este e-mail já está cadastrado.", file=sys.stderr)
            return 3
        db.add(User(email=email, full_name=args.name.strip(), password_hash=hash_password(password), is_platform_superuser=True, is_active=True, is_verified=True, organization_id=None))
        db.commit()
    print("Superusuário global criado com sucesso.")
    return 0

if __name__ == "__main__":
    raise SystemExit(create_superuser())
